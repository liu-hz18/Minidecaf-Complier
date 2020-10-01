# Generated from ./Expr.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete generic visitor for a parse tree produced by ExprParser.

class ExprVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ExprParser#program.
    def visitProgram(self, ctx:ExprParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#funcGlobalDeclare.
    def visitFuncGlobalDeclare(self, ctx:ExprParser.FuncGlobalDeclareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#symbolGlobalDeclare.
    def visitSymbolGlobalDeclare(self, ctx:ExprParser.SymbolGlobalDeclareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#funcDefine.
    def visitFuncDefine(self, ctx:ExprParser.FuncDefineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#funcDeclare.
    def visitFuncDeclare(self, ctx:ExprParser.FuncDeclareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#paramlist.
    def visitParamlist(self, ctx:ExprParser.ParamlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#paramDeclare.
    def visitParamDeclare(self, ctx:ExprParser.ParamDeclareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#scalar.
    def visitScalar(self, ctx:ExprParser.ScalarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#pointer.
    def visitPointer(self, ctx:ExprParser.PointerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#block.
    def visitBlock(self, ctx:ExprParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#SingleStatement.
    def visitSingleStatement(self, ctx:ExprParser.SingleStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#DeclareStatement.
    def visitDeclareStatement(self, ctx:ExprParser.DeclareStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#RetStatement.
    def visitRetStatement(self, ctx:ExprParser.RetStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#ExprStatement.
    def visitExprStatement(self, ctx:ExprParser.ExprStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#NullStatement.
    def visitNullStatement(self, ctx:ExprParser.NullStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#BlockStatement.
    def visitBlockStatement(self, ctx:ExprParser.BlockStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#IfStatement.
    def visitIfStatement(self, ctx:ExprParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#forNaiveStatement.
    def visitForNaiveStatement(self, ctx:ExprParser.ForNaiveStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#forDeclareStatement.
    def visitForDeclareStatement(self, ctx:ExprParser.ForDeclareStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#WhileStatement.
    def visitWhileStatement(self, ctx:ExprParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#doWhileStatement.
    def visitDoWhileStatement(self, ctx:ExprParser.DoWhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#BreakStatement.
    def visitBreakStatement(self, ctx:ExprParser.BreakStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#ContinueStatement.
    def visitContinueStatement(self, ctx:ExprParser.ContinueStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#declaration.
    def visitDeclaration(self, ctx:ExprParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#exprlist.
    def visitExprlist(self, ctx:ExprParser.ExprlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#expr.
    def visitExpr(self, ctx:ExprParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#SingleAssign.
    def visitSingleAssign(self, ctx:ExprParser.SingleAssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#ComplexAssign.
    def visitComplexAssign(self, ctx:ExprParser.ComplexAssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#SingleCond.
    def visitSingleCond(self, ctx:ExprParser.SingleCondContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#ComplexCond.
    def visitComplexCond(self, ctx:ExprParser.ComplexCondContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#ComplexOr.
    def visitComplexOr(self, ctx:ExprParser.ComplexOrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#SingleOr.
    def visitSingleOr(self, ctx:ExprParser.SingleOrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#SingleAnd.
    def visitSingleAnd(self, ctx:ExprParser.SingleAndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#ComplexAnd.
    def visitComplexAnd(self, ctx:ExprParser.ComplexAndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#SingleEq.
    def visitSingleEq(self, ctx:ExprParser.SingleEqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#ComplexEq.
    def visitComplexEq(self, ctx:ExprParser.ComplexEqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#ComplexRe.
    def visitComplexRe(self, ctx:ExprParser.ComplexReContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#SingleRe.
    def visitSingleRe(self, ctx:ExprParser.SingleReContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#ComplexAdd.
    def visitComplexAdd(self, ctx:ExprParser.ComplexAddContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#SingleAdd.
    def visitSingleAdd(self, ctx:ExprParser.SingleAddContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#SingleMul.
    def visitSingleMul(self, ctx:ExprParser.SingleMulContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#ComplexMul.
    def visitComplexMul(self, ctx:ExprParser.ComplexMulContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#SingleUnary.
    def visitSingleUnary(self, ctx:ExprParser.SingleUnaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#ComplexUnary.
    def visitComplexUnary(self, ctx:ExprParser.ComplexUnaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#Cast.
    def visitCast(self, ctx:ExprParser.CastContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#ComplexPostfix.
    def visitComplexPostfix(self, ctx:ExprParser.ComplexPostfixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#SinglePostfix.
    def visitSinglePostfix(self, ctx:ExprParser.SinglePostfixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#ArrayIndex.
    def visitArrayIndex(self, ctx:ExprParser.ArrayIndexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#atomInteger.
    def visitAtomInteger(self, ctx:ExprParser.AtomIntegerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#ComplexPrimary.
    def visitComplexPrimary(self, ctx:ExprParser.ComplexPrimaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#atomIdentifier.
    def visitAtomIdentifier(self, ctx:ExprParser.AtomIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#unOperator.
    def visitUnOperator(self, ctx:ExprParser.UnOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#addOperator.
    def visitAddOperator(self, ctx:ExprParser.AddOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#mulOperator.
    def visitMulOperator(self, ctx:ExprParser.MulOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#eqOperator.
    def visitEqOperator(self, ctx:ExprParser.EqOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#relOperator.
    def visitRelOperator(self, ctx:ExprParser.RelOperatorContext):
        return self.visitChildren(ctx)



del ExprParser