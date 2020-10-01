from overrides import overrides
from copy import deepcopy
import sys
from ast import literal_eval

from ..generated.ExprVisitor import ExprVisitor
from ..generated.ExprParser import ExprParser
from .ir_instructions import *
from .type import *
from .rule import *
from .name_visitor import NameInfo
from .variable import Variable

class TypeInfo():
    def __init__(self):
        self.ctx_type = {}
        self.ctx_location = {}
        self.func_ret_type = {}
        self.func_param_type = {}
        
    def getLvalueLocation(self, ctx):
        return self.ctx_location[ctx]
    
    def setLvalueLocation(self, ctx, loc:list):
        self.ctx_location[ctx] = loc
        
    def __getitem__(self, ctx):
        return self.ctx_type[ctx]
    
    def __setitem__(self, ctx, tp):
        self.ctx_type[ctx] = tp
        
    def __str__(self):
        return "\tctx_type: " + str(self.ctx_type) + "\n\tctx_location: " + str(self.ctx_location)


class TypeVisitor(ExprVisitor):
    def __init__(self, name_info:NameInfo):
        self.ni = name_info
        self.variableTypeMap = {}
        self._curFunction = None
        self.type_info = TypeInfo()
        self.lvalue_visitor = LValueVisitor(self.ni, self.type_info)

    def checkLValue(self, ctx):
        ret = ctx.accept(self.lvalue_visitor)
        if ret is None:
            raise Exception("lvalue expected.")
        self.type_info.setLvalueLocation(ctx, ret)
        
    @overrides
    def visitChildren(self, ctx):
        tp = ExprVisitor.visitChildren(self, ctx)
        self.type_info[ctx] = tp
        return tp
    
    @overrides
    def visitScalar(self, ctx):
        return IntType()
    
    @overrides
    def visitPointer(self, ctx):
        return PointerType(ctx.tp().accept(self))
    
    @overrides
    def visitCast(self, ctx):
        ctx.unary().accept(self)
        tp = ctx.tp().accept(self)
        self.type_info[ctx] = tp
        return tp
    
    @overrides
    def visitComplexUnary(self, ctx):
        # check for lvalue '&'
        # path to `ComplexUnary, `atomIdentifier ArrayIndex`
        # only fall into one function
        # not need to build a new visitor
        # only some effort
        tp = ruleUnaryFuncMap[str(ctx.unOperator().getText())](ctx.unary().accept(self))
        if str(ctx.unOperator().getText()) == '&':
            self.checkLValue(ctx.unary())
        self.type_info[ctx] = tp
        return tp
    
    @overrides
    def visitComplexAdd(self, ctx):
        tp = ruleBinaryFuncMap[str(ctx.addOperator().getText())](ctx.additive().accept(self), ctx.multiplicative().accept(self))
        self.type_info[ctx] = tp
        return tp
    
    @overrides
    def visitComplexAnd(self, ctx):
        tp = ruleBinaryFuncMap['&&'](ctx.logicalAnd().accept(self), ctx.equality().accept(self))
        self.type_info[ctx] = tp
        return tp
    
    @overrides
    def visitComplexOr(self, ctx):
        tp = ruleBinaryFuncMap['||'](ctx.logicalOr().accept(self), ctx.logicalAnd().accept(self))
        self.type_info[ctx] = tp
        return tp
    
    @overrides
    def visitComplexMul(self, ctx):
        tp = ruleBinaryFuncMap[str(ctx.mulOperator().getText())](ctx.multiplicative().accept(self), ctx.unary().accept(self))
        self.type_info[ctx] = tp
        return tp
    
    @overrides
    def visitComplexAssign(self, ctx):
        # check for lvalue '='
        # path to `ComplexUnary, ArrayIndex, AtomIdentifier, ComplexPrimary`
        # only fall into one function
        # not need to build a new visitor
        # only some effort
        tp = ruleBinaryFuncMap['='](ctx.unary().accept(self), ctx.expr().accept(self))
        self.checkLValue(ctx.unary())
        self.type_info[ctx] = tp
        return tp
    
    @overrides
    def visitComplexEq(self, ctx):
        tp = ruleBinaryFuncMap[str(ctx.eqOperator().getText())](ctx.equality().accept(self), ctx.relational().accept(self))
        self.type_info[ctx] = tp
        return tp
    
    @overrides
    def visitComplexRe(self, ctx):
        tp =  ruleBinaryFuncMap[str(ctx.relOperator().getText())](ctx.relational().accept(self), ctx.additive().accept(self))
        self.type_info[ctx] = tp
        return tp
    
    @overrides
    def visitComplexCond(self, ctx):
        tp = conditionRule(ctx.logicalOr().accept(self), ctx.expr().accept(self), ctx.conditional().accept(self))
        self.type_info[ctx] = tp
        return tp
    
    @overrides
    def visitComplexPrimary(self, ctx):
        tp =  ctx.expr().accept(self)
        self.type_info[ctx] = tp
        return tp
    
    @overrides
    def visitArrayIndex(self, ctx):
        tp =  arrayIndexRule(ctx.postfix().accept(self), ctx.expr().accept(self))
        self.type_info[ctx] = tp
        return tp

    @overrides
    def visitAtomInteger(self, ctx):
        tp = IntType()
        self.type_info[ctx] = tp
        return tp
    
    @overrides
    def visitAtomIdentifier(self, ctx):
        variable = self.ni[ctx.Identifier()]
        tp = self.type_info[ctx] = self.variableTypeMap[variable]
        return tp
    
    @overrides
    def visitParamDeclare(self, ctx):
        variable = self.ni[ctx.Identifier()]
        real_type = ctx.tp().accept(self)
        self.variableTypeMap[variable] = real_type
    
    @overrides
    def visitDeclaration(self, ctx):
        variable = self.ni[ctx.Identifier()]
        real_type = self._declareType(ctx)
        self.variableTypeMap[variable] = real_type
        if ctx.expr() is not None:
            value_type = ctx.expr().accept(self)
            opAssignRule(real_type, value_type)
    
    def _declareType(self, ctx):
        base_type = ctx.tp().accept(self)
        dims = [int(x.getText()) for x in reversed(ctx.Integer())]
        if len(dims) == 0:
            real_type = base_type
        else:
            real_type = ArrayType(base_type, dims).unwarp()
        return real_type
    
    def _paramList(self, ctx):
        types = []
        for declare in ctx.paramDeclare():
            paramType = declare.tp().accept(self)
            types.append(paramType)
        return types
    
    def checkFunction(self, ctx):
        ret_type = ctx.tp().accept(self)
        param_types = self._paramList(ctx.paramlist())
        func_name = str(ctx.Identifier().getText())
        if func_name in self.type_info.func_param_type:
            if self.type_info.func_param_type[func_name] != param_types or \
                self.type_info.func_ret_type[func_name] != ret_type:
                    raise Exception(f"function `{func_name}` param/ret type conficting.")    
        else:
            self.type_info.func_param_type[func_name] = param_types
            self.type_info.func_ret_type[func_name] = ret_type
        
    @overrides
    def visitFuncDeclare(self, ctx):
        func_name = str(ctx.Identifier().getText())
        self._curFunction = func_name
        self.checkFunction(ctx)
        self._curFunction = None
    
    @overrides
    def visitFuncDefine(self, ctx):
        func_name = str(ctx.Identifier().getText())
        self._curFunction = func_name
        self.checkFunction(ctx)
        self.visitChildren(ctx)
        self._curFunction = None
    
    @overrides # call function
    def visitComplexPostfix(self, ctx):
        args_type = list(map(lambda x: x.accept(self), ctx.exprlist().expr()))
        func_name = str(ctx.Identifier().getText())
        func_param_type = self.type_info.func_param_type[func_name]
        if args_type != func_param_type:
            raise Exception(f"function `{func_name}({','.join(map(str, func_param_type))})` args and params type mismatch.")
        tp = self.type_info[ctx] = self.type_info.func_ret_type[func_name]
        return tp
    
    @overrides
    def visitSymbolGlobalDeclare(self, ctx):
        decl_ctx = ctx.declaration()
        var_str = str(decl_ctx.Identifier().getText())
        # v = Variable(var_str, None, INT_BYTES)
        v = self.ni.globals[var_str].variable
        tp = self._declareType(decl_ctx)
        if v in self.variableTypeMap:
            prev_type = self.variableTypeMap[v]
            if prev_type != tp:
                raise Exception(f"global varible {var_str} type conficting.")
        else:
            self.variableTypeMap[v] = tp
        if decl_ctx.expr() is not None:
            value_type = decl_ctx.expr().accept(self)
            opAssignRule(tp, value_type)
    
    @overrides
    def visitIfStatement(self, ctx):
        self.visitChildren(ctx)
        intRule(ctx.expr().accept(self))
    
    @overrides
    def visitForDeclareStatement(self, ctx):
        self.visitChildren(ctx)
        if ctx.cond is not None:
            intRule(ctx.cond.accept(self))
    
    @overrides
    def visitDoWhileStatement(self, ctx):
        self.visitChildren(ctx)
        intRule(ctx.expr().accept(self))
    
    @overrides
    def visitWhileStatement(self, ctx):
        self.visitChildren(ctx)
        intRule(ctx.expr().accept(self))
            
    @overrides
    def visitForNaiveStatement(self, ctx):
        self.visitChildren(ctx)
        if ctx.cond is not None:
            intRule(ctx.cond.accept(self))

    @overrides
    def visitRetStatement(self, ctx):
        func_ret_type = self.type_info.func_ret_type[self._curFunction]
        callee_real_type = ctx.expr().accept(self)
        returnRule(func_ret_type, callee_real_type)

    
class LValueVisitor(ExprVisitor):
    def __init__(self, name_info:NameInfo, type_info:TypeInfo):
        self.name_info = name_info
        self.type_info = type_info
    
    def visitAtomIdentifier(self, ctx):
        variable = self.name_info[ctx.Identifier()]
        if variable.offset is None:
            return [IrGlobalAddr(variable.ident)]
        else:
            return [IrFrameAddr(variable.offset)]
    
    def visitComplexUnary(self, ctx):
        op = str(ctx.unOperator().getText())
        if op == '*':
            return [ctx.unary()]
    
    def visitComplexPrimary(self, ctx):
        return ctx.expr().accept(self)
    
    def visitArrayIndex(self, ctx):
        total_size = self.type_info[ctx.postfix()].base.sizeof()
        return [ctx.postfix(), ctx.expr(), IrConst(total_size), IrBinary('*'), IrBinary('+')]
