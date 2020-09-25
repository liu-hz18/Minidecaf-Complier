from ..generated.ExprVisitor import ExprVisitor
from ..generated.ExprParser import ExprParser
from .ir_instructions import *
from overrides import overrides

class StackIRVisitor(ExprVisitor):
    def __init__(self):
        super(StackIRVisitor, self).__init__()
        self.ir_instructions = []
       
    @overrides
    def visitStatement(self, ctx:ExprParser.StatementContext):
        self.visitChildren(ctx)
        self.ir_instructions.append(IrRet())

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
        
    def getIR(self):
        return "main:\n\t" + '\n\t'.join(map(str, self.ir_instructions))
