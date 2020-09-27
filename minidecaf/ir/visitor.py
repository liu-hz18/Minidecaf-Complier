from ..generated.ExprVisitor import ExprVisitor
from ..generated.ExprParser import ExprParser
from .ir_instructions import *
from overrides import overrides
from copy import deepcopy
import sys
from ast import literal_eval

class Variable():
    _var_counter = {}
    def __init__(self, identifier:str, offset:int, size:int=INT_BYTES):
        if identifier in Variable._var_counter:
            Variable._var_counter[identifier] += 1
        else:
            Variable._var_counter[identifier] = 0
        self.uid = Variable._var_counter[identifier]
        self.ident = identifier
        self.offset = offset
        self.size = size
    
    def __str__(self):
        return f"{self.ident}({self.uid}{self.offset})"
    
    def __repr__(self):
        return self.__str__()

    def __hash__(self):
        return hash((self.ident, self.id, self.offset, self.size))

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
        self._curNSlots += 1
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
        self._curFuncNameInfo.blockSlots[ctx] = self._curNSlots - self._nSlots[-1]
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
            raise Exception(f"function <{var}(...)> redeclared as gloabl variable")
        v = Variable(var, None, INT_BYTES)
        globalIr = IrGlobalSymbol(var, init, INT_BYTES)
        # check for redefinition
        if var in self._v.top():
            prevGlobalIr = self.nameInfo.globals[var]
            if prevGlobalIr.value is not None and globalIr.value is not None:
                raise Exception(f"global symbol {var} redefinition")
            if globalIr.value is not None:
                self.nameInfo.globals[var].value = value
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
        self.defVar(ctx, varstr, number=1)
    
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
        

class StackIRVisitor(ExprVisitor):
    label_counter = {}
    def __init__(self, nameInfo:NameInfo):
        super(StackIRVisitor, self).__init__()
        self.ir_instructions = []
        self.funcs = []
        self.curFuncName = None
        self.curFuncParams = None
        self.ni = nameInfo
        self.loopStart = []
        self.loopEnd = []
        self.declared_func = []
        # labels
        self.initGlobalIrs()
    
    def initGlobalIrs(self):
        self.glob_def, self.glob_dec = [], []
        for glob in self.ni.globals.values():
            if glob.value is not None:
                self.glob_def.append(glob)
            else:
                self.glob_dec.append(glob)

    @property
    def breakLabel(self):
        if len(self.loopEnd) <= 0:
            raise Exception("break not in a loop")
        return self.loopEnd[-1]
    
    @property    
    def continueLabel(self):
        if len(self.loopEnd) <= 0:
            raise Exception("continue not in a loop")
        return self.loopStart[-1]
    
    def _createLabel(self, label="_L"):
        if label in StackIRVisitor.label_counter:
            StackIRVisitor.label_counter[label] += 1
        else:
            StackIRVisitor.label_counter[label] = 0
        return f"{label}_{StackIRVisitor.label_counter[label]}"

    def _loop(self, name, pre, condition, body, post):
        loopLabel = self._createLabel(f"{name}_pre")
        if post is not None:
            continueLabel = self._createLabel(f"{name}_continue")
        else:
            continueLabel = loopLabel
        endLabel = self._createLabel(f"{name}_end")
        self.loopStart.append(continueLabel)
        self.loopEnd.append(endLabel)
        if pre is not None:
            pre.accept(self)
            if isinstance(pre, ExprParser.ExprContext):
                self.ir_instructions.append(IrPop())
        self.ir_instructions.append(IrLabel(loopLabel))
        if condition is not None:
            condition.accept(self)
        else:
            self.ir_instructions.append(IrConst(1))
        self.ir_instructions.append(IrBranch("beqz", endLabel))
        body.accept(self)
        if post is not None:
            self.ir_instructions.append(IrLabel(continueLabel))
            post.accept(self)
            if isinstance(post, ExprParser.ExprContext):
                self.ir_instructions.append(IrPop())
        self.ir_instructions.append(IrBranch("br", loopLabel))
        self.ir_instructions.append(IrLabel(endLabel))
        self.loopStart.pop()
        self.loopEnd.pop()
    
    def checkFuncCall(self, funcName, argc):
        for fun in self.declared_func:
            if funcName == fun.name:
                if argc != fun.nParams:
                    raise Exception(f"function <{funcDec}({argc})> not defined.")
        for fun in self.funcs:
            if funcName == fun.name:
                if argc != fun.nParams:
                    raise Exception(f"function <{funcDec}({argc})> not defined.")
    
    @overrides
    def visitComplexPostfix(self, ctx:ExprParser.ComplexPostfixContext):
        funcName = str(ctx.Identifier().getText())
        args = ctx.exprlist().expr()
        self.checkFuncCall(funcName, len(args))
        for arg in reversed(args):
            arg.accept(self)
        self.ir_instructions.append(IrCall(funcName))
        
    @overrides
    def visitForDeclareStatement(self, ctx:ExprParser.ForDeclareStatementContext):
        self._loop("for", ctx.pre, ctx.cond, ctx.statement(), ctx.post)
        self.ir_instructions.extend([IrPop()] * self.ni.funcs[self.curFuncName].blockSlots[ctx])
    
    @overrides
    def visitForNaiveStatement(self, ctx):
        self._loop("for", ctx.pre, ctx.cond, ctx.statement(), ctx.post)
    
    @overrides
    def visitWhileStatement(self, ctx):
        self._loop("while", None, ctx.expr(), ctx.statement(), None)
    
    @overrides
    def visitDoWhileStatement(self, ctx):
        self._loop("dowhile", ctx.statement(), ctx.expr(), ctx.statement(), None)
    
    @overrides
    def visitBreakStatement(self, ctx):
        self.ir_instructions.append(IrBranch("br", self.breakLabel))
    
    @overrides
    def visitContinueStatement(self, ctx):
        self.ir_instructions.append(IrBranch("br", self.continueLabel))
    
    @overrides
    def visitBlock(self, ctx):
        self.visitChildren(ctx)
        self.ir_instructions.extend([IrPop()] * self.ni.funcs[self.curFuncName].blockSlots[ctx])

    def _declareType(self, ctx):
        baseType = str(ctx.tp().getText())
        return baseType

    def _paramList(self, ctx):
        types, names = [], []
        for declare in ctx.paramDeclare():
            paramType = self._declareType(declare)
            paramName = str(declare.Identifier().getText())
            types.append(paramType)
            names.append(paramName)
        return types, names
    
    def checkFuncDeclare(self, func:IrFunction):
        funcDec = func.name
        for fun in self.declared_func:
            if funcDec == fun.name:
                if func != fun:
                    raise Exception(f"function <{funcDec}(...)> declaration and definition don't match.")

    def checkFuncDefine(self, func:IrFunction):
        funcDec = func.name
        for fun in self.funcs:
            if funcDec == fun.name:
                if func != fun:
                    raise Exception(f"function <{funcDec}(...)> declaration and definition don't match.")
    
    @overrides
    def visitFuncDefine(self, ctx:ExprParser.FuncDefineContext):
        func = str(ctx.Identifier().getText())
        # nParams
        param_types, param_names = self._paramList(ctx.paramlist())
        nParams = len(param_names)
        if len(set(param_names)) != nParams:
            raise Exception(f"function <{func}> parameter conflicted.")
        # enter
        self.curFuncName = func
        self.curFuncParams = nParams
        self.ir_instructions = []
        self.visitChildren(ctx)
        function = IrFunction(func, nParams, self.ir_instructions, param_types)
        self.checkFuncDeclare(function)
        # exit
        self.funcs.append(function)
        self.curFuncName = None
    
    @overrides
    def visitFuncDeclare(self, ctx:ExprParser.FuncDeclareContext):
        funcDec = str(ctx.Identifier().getText())
        # nParams
        param_types, param_names = self._paramList(ctx.paramlist())
        nParams = len(param_names)
        if len(set(param_names)) != nParams:
            raise Exception(f"function <{func}> parameter conflicted.")
        function = IrFunction(funcDec, nParams, [], param_types)
        self.checkFuncDefine(function)
        self.declared_func.append(function)
    
    @overrides
    def visitComplexCond(self, ctx:ExprParser.ComplexCondContext):
        ctx.logicalOr().accept(self)
        endLabel = self._createLabel("cond_end")
        elseLabel = self._createLabel("cond_else")
        self.ir_instructions.append(IrBranch("beqz", elseLabel))
        
        ctx.expr().accept(self)
        self.ir_instructions.append(IrBranch("br", endLabel))
        self.ir_instructions.append(IrLabel(elseLabel))
        
        ctx.conditional().accept(self)
        self.ir_instructions.append(IrLabel(endLabel))
    
    @overrides
    def visitIfStatement(self, ctx:ExprParser.IfStatementContext):
        ctx.expr().accept(self)
        endLabel = self._createLabel("if_end")
        elseLabel = self._createLabel("if_else")
        if ctx.elses is not None:
            self.ir_instructions.append(IrBranch("beqz", elseLabel))
            ctx.thens.accept(self)
            self.ir_instructions.append(IrBranch("br", endLabel))
            self.ir_instructions.append(IrLabel(elseLabel))
            ctx.elses.accept(self)
            self.ir_instructions.append(IrLabel(endLabel))
        else:
            self.ir_instructions.append(IrBranch("beqz", endLabel))
            ctx.thens.accept(self)
            self.ir_instructions.append(IrLabel(endLabel))
    
    @overrides
    def visitRetStatement(self, ctx:ExprParser.RetStatementContext):
        self.visitChildren(ctx)
        self.ir_instructions.append(IrRet())
    
    @overrides
    def visitExprStatement(self, ctx:ExprParser.ExprStatementContext):
        self.visitChildren(ctx)
        self.ir_instructions.append(IrPop())
   
    @overrides
    def visitSymbolGlobalDeclare(self, ctx):
        pass

    @overrides
    def visitDeclaration(self, ctx:ExprParser.DeclareStatementContext):
        var = self.ni[ctx.Identifier()]
        if ctx.expr() is not None:
            ctx.expr().accept(self)
        else:
            self.ir_instructions.extend([IrConst(0)] * (var.size // INT_BYTES))
    
    def _findIdentifier(self, ctx):
        if isinstance(ctx, ExprParser.SingleUnaryContext):
            return self._findIdentifier(ctx.postfix())
        elif isinstance(ctx, ExprParser.SinglePostfixContext):
            return self._findIdentifier(ctx.primary())
        elif isinstance(ctx, ExprParser.PrimaryContext):
            return ctx.Identifier()
    
    @overrides
    def visitComplexAssign(self, ctx:ExprParser.ComplexAssignContext):
        ctx.expr().accept(self)
        var = self.ni[self._findIdentifier(ctx.unary())]
        # ident
        if var.offset is None:
            self.ir_instructions.append(IrGlobalAddr(var.ident))
        else:
            self.ir_instructions.append(IrFrameAddr(var.offset))
        self.ir_instructions.append(IrStore())
    
    @overrides
    def visitAtomIdentifier(self, ctx:ExprParser.AtomIdentifierContext):
        var = self.ni[ctx.Identifier()]
        if var.offset is None:
            self.ir_instructions.append(IrGlobalAddr(var.ident))
        else:
            self.ir_instructions.append(IrFrameAddr(var.offset))
        self.ir_instructions.append(IrLoad())
    
    @overrides
    def visitAtomInteger(self, ctx:ExprParser.AtomIntegerContext):
        v = int(str(ctx.Integer().getText()))
        self.ir_instructions.append(IrConst(v))
    
    def _visitBinary(self, op, ctx):
        self.visitChildren(ctx)
        self.ir_instructions.append(IrBinary(op))

    @overrides
    def visitComplexOr(self, ctx:ExprParser.ComplexOrContext):
        self.visitChildren(ctx)
        self.ir_instructions.append(IrBinary("||"))
        
    @overrides
    def visitComplexAnd(self, ctx:ExprParser.ComplexAndContext):
        self.visitChildren(ctx)
        self.ir_instructions.append(IrBinary("&&"))

    @overrides
    def visitComplexEq(self, ctx:ExprParser.ComplexEqContext):
        op = str(ctx.eqOperator().getText())
        self._visitBinary(op, ctx)

    @overrides
    def visitComplexRe(self, ctx:ExprParser.ComplexReContext):
        op = str(ctx.relOperator().getText())
        self._visitBinary(op, ctx)
    
    @overrides
    def visitComplexAdd(self, ctx:ExprParser.ComplexAddContext):
        op = str(ctx.addOperator().getText())
        self._visitBinary(op, ctx)

    @overrides
    def visitComplexMul(self, ctx:ExprParser.ComplexMulContext):
        op = str(ctx.mulOperator().getText())
        self._visitBinary(op, ctx)

    @overrides
    def visitComplexUnary(self, ctx:ExprParser.ComplexUnaryContext):
        op = str(ctx.unOperator().getText())
        self.visitChildren(ctx)
        self.ir_instructions.append(IrUnary(op))

    @overrides
    def visitComplexPrimary(self, ctx:ExprParser.ComplexPrimaryContext):
        return self.visitChildren(ctx)
        
    @overrides
    def visitProgram(self, ctx:ExprParser.ProgramContext):
        self.visitChildren(ctx)    
    
    def getIR(self):
        return '\n'.join([
            str(func) for func in self.funcs
        ])
