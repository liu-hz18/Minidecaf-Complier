from overrides import overrides
from copy import deepcopy
import sys
from ast import literal_eval

from ..generated.ExprVisitor import ExprVisitor
from ..generated.ExprParser import ExprParser
from .ir_instructions import *
from .name_visitor import *
from .type_visitor import *
from .info import *

class StackIRVisitor(ExprVisitor):
    label_counter = {}
    def __init__(self, name_info:NameInfo, type_info:TypeInfo):
        super(StackIRVisitor, self).__init__()
        self.ir_instructions = []
        self.funcs = []
        self.curFuncName = None
        self.curFuncParams = None
        self.ni = name_info
        self.ti = type_info
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
        ret_type = str(ctx.tp().getText())
        nParams = len(param_names)
        if len(set(param_names)) != nParams:
            raise Exception(f"function <{func}> parameter conflicted.")
        # enter
        self.curFuncName = func
        self.curFuncParams = nParams
        self.ir_instructions = []
        self.visitChildren(ctx)
        function = IrFunction(func, nParams, self.ir_instructions, param_types, ret_type)
        self.checkFuncDeclare(function)
        # exit
        self.funcs.append(function)
        self.curFuncName = None
    
    @overrides
    def visitFuncDeclare(self, ctx:ExprParser.FuncDeclareContext):
        funcDec = str(ctx.Identifier().getText())
        # nParams
        param_types, param_names = self._paramList(ctx.paramlist())
        ret_type = str(ctx.tp().getText())
        nParams = len(param_names)
        if len(set(param_names)) != nParams:
            raise Exception(f"function <{func}> parameter conflicted.")
        function = IrFunction(funcDec, nParams, [], param_types, ret_type)
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
        lvalue_loc = self.ti.getLvalueLocation(ctx.unary())
        for loc in lvalue_loc:
            if isinstance(loc, IrBaseInstraction):
                self.ir_instructions.append(loc)
            else:
                loc.accept(self)
        self.ir_instructions.append(IrStore())
    
    @overrides
    def visitAtomIdentifier(self, ctx:ExprParser.AtomIdentifierContext):
        var = self.ni[ctx.Identifier()]
        if var.offset is None:
            self.ir_instructions.append(IrGlobalAddr(var.ident))
        else:
            self.ir_instructions.append(IrFrameAddr(var.offset))
        if not isinstance(self.ti[ctx], OneDimArrayType):
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
    
    def intAddOrSubPtr(self, op, left, right):
        size = self.ti[right].sizeof()
        left.accept(self)
        self.ir_instructions.extend([IrConst(size), IrBinary('*')])
        right.accept(self)
        self.ir_instructions.append(IrBinary(op))
    
    def ptrAddOrSubInt(self, op, left, right):
        left.accept(self)
        right.accept(self)
        size = self.ti[left].sizeof()
        self.ir_instructions.extend([IrConst(size), IrBinary('*'), IrBinary(op)])
        
    def prtSubPtr(self, op, left, right):
        left.accept(self)
        right.accept(self)
        size = self.ti[left].sizeof()
        self.ir_instructions.extend([IrBinary(op), IrConst(size), IrBinary('/')])
    
    @overrides
    def visitComplexAdd(self, ctx:ExprParser.ComplexAddContext):
        op = str(ctx.addOperator().getText())
        left = ctx.additive()
        right = ctx.multiplicative()
        
        if isinstance(self.ti[left], PointerType):
            if isinstance(self.ti[right], PointerType):
                self.prtSubPtr(op, left, right)
            else:
                self.ptrAddOrSubInt(op, left, right)
        else:
            if isinstance(self.ti[right], PointerType):
                self.intAddOrSubPtr(op, left, right)
            else:
                self.visitChildren(ctx)
                self.ir_instructions.append(IrBinary(op))

    @overrides
    def visitComplexMul(self, ctx:ExprParser.ComplexMulContext):
        op = str(ctx.mulOperator().getText())
        self._visitBinary(op, ctx)

    @overrides
    def visitComplexUnary(self, ctx:ExprParser.ComplexUnaryContext):
        op = str(ctx.unOperator().getText())
        if op == '&':
            lvalue_loc = self.ti.getLvalueLocation(ctx.unary())
            for loc in lvalue_loc:
                if isinstance(loc, IrBaseInstraction):
                    self.ir_instructions.append(loc)
                else:
                    loc.accept(self)
        elif op == '*':
            self.visitChildren(ctx)
            self.ir_instructions.append(IrLoad())
        else:
            self.visitChildren(ctx)
            self.ir_instructions.append(IrUnary(op))

    @overrides
    def visitComplexPrimary(self, ctx:ExprParser.ComplexPrimaryContext):
        return self.visitChildren(ctx)
    
    @overrides
    def visitArrayIndex(self, ctx):
        n_elems = self.ti[ctx.postfix()].base.sizeof()
        ctx.postfix().accept(self)
        ctx.expr().accept(self)
        self.ir_instructions.extend([
            IrConst(n_elems), IrBinary('*'), IrBinary('+')
        ])
        if not isinstance(self.ti[ctx], OneDimArrayType):
            self.ir_instructions.append(IrLoad())
    
    @overrides
    def visitProgram(self, ctx:ExprParser.ProgramContext):
        self.visitChildren(ctx)    
    
    def getIR(self):
        return '\n'.join([
            str(func) for func in self.funcs
        ])
