from overrides import overrides
from copy import deepcopy
import sys
from ast import literal_eval

from ..generated.ExprVisitor import ExprVisitor
from ..generated.ExprParser import ExprParser
from .ir_instructions import *
from .variable import Variable


class NameInfo():
    def __init__(self):
        self.var = {}
        self.funcs = {}
        self.globals = {}

    def freeze(self):
        for funcNameInfo in self.funcs.values():
            self.var.update(funcNameInfo.var)

    def __getitem__(self, ctx):
        return self.var[ctx]

    def __str__(self):
        return "\tvar: " + str(self.var) + "\n\tfuncs: " + str(self.funcs) + "\n\tglobals: " + str(self.globals)

    def __repr__(self):
        return self.__str__()


class FuncNameInfo():
    def __init__(self, hasDef=True):
        self.var = {}
        self.pos = {}
        self.blockSlots = {}
        self.hasDef = hasDef

    def bind(self, varstr, var, pos):
        self.var[varstr] = var
        self.pos[varstr] = pos

    def __str__(self):
        return str(self.var) + str(self.hasDef)

    def __repr__(self):
        return self.__str__()

    def __getitem__(self, varstr):
        return self.var[varstr]


class StackDict():
    def __init__(self):
        self.accumulated_stack = [{}]
        self.cur_stack = [{}]

    def __getitem__(self, key):
        return self.accumulated_stack[-1][key]

    def __setitem__(self, key, value):
        self.accumulated_stack[-1][key] = self.cur_stack[-1][key] = value

    def __contains__(self, key):
        return key in self.accumulated_stack[-1]

    def __len__(self):
        return len(self.accumulated_stack[-1])

    def push(self):
        self.accumulated_stack.append(deepcopy(self.accumulated_stack[-1]))
        self.cur_stack.append({})

    def pop(self):
        self.accumulated_stack.pop()
        self.cur_stack.pop()

    def top(self):
        return self.cur_stack[-1]


class NameVisitor(ExprVisitor):
    def __init__(self):
        super(NameVisitor, self).__init__()
        self.nameInfo = NameInfo()
        self._curFuncNameInfo = None
        self._curNSlots = 0
        self._v = StackDict()
        self._nSlots = []

    def defVar(self, ctx, varstr, number=1):
        self._curNSlots += number
        var = self._v[varstr] = Variable(varstr,
                                         -INT_BYTES * self._curNSlots, INT_BYTES * number)
        pos = (ctx.start.line, ctx.start.column)
        self._curFuncNameInfo.bind(ctx.Identifier(), var, pos)

    def useVar(self, ctx, varstr):
        var = self._v[varstr]
        pos = (ctx.start.line, ctx.start.column)
        self._curFuncNameInfo.bind(ctx.Identifier(), var, pos)

    def enterScope(self, ctx):
        self._v.push()
        self._nSlots.append(self._curNSlots)

    def exitScope(self, ctx):
        self._curFuncNameInfo.blockSlots[ctx] = self._curNSlots - \
            self._nSlots[-1]
        self._curNSlots = self._nSlots[-1]
        self._v.pop()
        self._nSlots.pop()

    @overrides
    def visitSymbolGlobalDeclare(self, ctx):
        ctx = ctx.declaration()
        init = None
        if ctx.expr() is not None:
            expr = str(ctx.expr().getText())
            try:
                init = literal_eval(expr)
            except:
                raise Exception("global symbol initialization must be contant")
        var = str(ctx.Identifier().getText())
        if var in self.nameInfo.funcs:
            raise Exception(
                f"function <{var}(...)> redeclared as gloabl variable")
        n_elems = 1
        for integer_str in ctx.Integer():
            n_elems *= int(integer_str.getText())
        if n_elems <= 0:
            raise Exception("array size < 0")
        if n_elems >= MAX_INT:
            raise Exception("array size is too large")
        
        v = Variable(var, None, INT_BYTES * n_elems)
        globalIr = IrGlobalSymbol(var, init, v, INT_BYTES*n_elems)
        # check for redefinition
        if var in self._v.top():
            prevGlobalIr = self.nameInfo.globals[var]
            if prevGlobalIr.init is not None and globalIr.init is not None:
                raise Exception(f"global symbol {var} redefinition")
            if globalIr.variable is not None:
                self.nameInfo.globals[var].init = init
        else:
            self._v[var] = v
            self.nameInfo.globals[var] = globalIr

    @overrides
    def visitBlock(self, ctx):
        self.enterScope(ctx)
        self.visitChildren(ctx)
        self.exitScope(ctx)

    @overrides
    def visitDeclaration(self, ctx):
        if ctx.expr() is not None:
            ctx.expr().accept(self)
        varstr = str(ctx.Identifier().getText())
        if varstr in self._v.top():
            raise Exception(f"redefinition of variable `{varstr}`")
        # array declaration
        n_elems = 1
        for integer_str in ctx.Integer():
            n_elems *= int(integer_str.getText())
        if n_elems <= 0:
            raise Exception("array size < 0")
        if n_elems >= MAX_INT:
            raise Exception("array size is too large")
        self.defVar(ctx, varstr, number=n_elems)

    @overrides
    def visitForDeclareStatement(self, ctx):
        self.enterScope(ctx)
        self.visitChildren(ctx)
        self.exitScope(ctx)

    @overrides
    def visitAtomIdentifier(self, ctx):
        varstr = str(ctx.Identifier().getText())
        if varstr not in self._v:
            raise Exception(f"variable `{varstr}` not declared")
        self.useVar(ctx, varstr)

    @overrides
    def visitParamDeclare(self, ctx):
        varstr = str(ctx.Identifier().getText())
        self.defVar(ctx, varstr, number=1)

    @overrides
    def visitFuncDefine(self, ctx):
        funcName = str(ctx.Identifier().getText())
        if funcName in self.nameInfo.funcs and self.nameInfo.funcs[funcName].hasDef:
            raise Exception(f"redefnition of function `{funcName}`")
        funcNameInfo = FuncNameInfo(hasDef=True)
        self._curFuncNameInfo = self.nameInfo.funcs[funcName] = funcNameInfo
        self.enterScope(ctx.block())
        self.visitChildren(ctx.paramlist())
        self.visitChildren(ctx.block())
        self.exitScope(ctx.block())
        self._curFuncNameInfo = None

    @overrides
    def visitFuncDeclare(self, ctx):
        funcName = str(ctx.Identifier().getText())
        funcNameInfo = FuncNameInfo(hasDef=False)
        # slove redeclaration
        for func in self.nameInfo.globals:
            raise Exception(f"global variable {func} redeclared as function")
        if funcName not in self.nameInfo.funcs:
            self.nameInfo.funcs[funcName] = funcNameInfo

    @overrides
    def visitProgram(self, ctx):
        self.visitChildren(ctx)
        self.nameInfo.freeze()
