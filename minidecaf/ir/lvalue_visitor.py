from overrides import overrides

from ..generated.ExprVisitor import ExprVisitor
from .ir_instructions import *
from .type import *
from .rule import *
from .name_visitor import NameInfo
from .variable import Variable
from .type_visitor import TypeInfo

class LValueVisitor(ExprVisitor):
    def __init__(self, name_info:NameInfo, type_info:TypeInfo):
        self.name_info = name_info
        self.type_info = type_info
    
    @overrides
    def visitAtomIdentifier(self, ctx):
        variable = self.name_info[ctx.Identifier()]
        if variable.offset is None:
            return [IrGlobalAddr(variable.ident)]
        else:
            return [IrFrameAddr(variable.offset)]
    
    @overrides
    def visitComplexUnary(self, ctx):
        op = str(ctx.unOperator().getText())
        if op == '*':
            return [ctx.unary()]
    
    @overrides
    def visitComplexPrimary(self, ctx):
        return ctx.expr().accept(self)
    
    @overrides
    def visitArrayIndex(self, ctx):
        total_size = self.type_info[ctx.postfix()].base.sizeof()
        return [ctx.postfix(), ctx.expr(), IrConst(total_size), IrBinary('*'), IrBinary('+')]
