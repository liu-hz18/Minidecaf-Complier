"""实例：真·main"""
import sys
import os
import argparse
from overrides import overrides
from antlr4 import *

from .generated.ExprLexer import ExprLexer
from .generated.ExprParser import ExprParser
from .generated.ExprVisitor import ExprVisitor

INT_BYTES = 4
MAX_INT = 2**(INT_BYTES*8-1) - 1
#MIN_INT = -2**(INT_BYTES*8)
MIN_INT = 0
unAryMap = {
    '~': 'not',
    '!': 'seqz',
    '-': 'neg',
}
binaryMap = {
    '+': 'add',
    '-': 'sub',
    '*': 'mul',
    '/': 'div',
    '%': 'rem',
    '<': 'slt',
    '>': 'sgt',
    '<=': 'slet',
    '>=': 'sget',
    '==': 'eq',
    '!=': 'ne',
    '&&': 'land',
    '||': 'lor',
}
oneInsBinaryList = [
    'add',
    'sub',
    'mul',
    'div',
    'rem',
    'slt',
    'sgt',
]

class IrBaseInstraction():
    def __repr__(self):
        return self.__str__()


class IrConst(IrBaseInstraction):
    def __init__(self, v:int):
        assert MIN_INT <= v < MAX_INT
        self.v = v

    def __str__(self):
        return f"pushi {self.v}"


class IrRet(IrBaseInstraction):
    def __str__(self):
        return f"ret"


class IrUnary(IrBaseInstraction):
    def __init__(self, op):
        assert op in unAryMap
        self.op = unAryMap[op]
    
    def __str__(self):
        return self.op
        
class IrBinary(IrBaseInstraction):
    def __init__(self, op):
        assert op in binaryMap
        self.op = binaryMap[op]
    
    def __str__(self):
        return self.op

class AsmBase():
    def __init__(self, s):
        self.s = s

    def __repr__(self):
        return self.__str__()

class AsmInstruction(AsmBase):
    def __str__(self):
        return f"\t{self.s}"

class AsmLabel(AsmBase):
    def __str__(self):
        return f"{self.s}:"
    
class AsmComment(AsmBase):
    def __str__(self):
        return f"\t#{self.s}"
    
class AsmDirective(AsmBase):
    def __str__(self):
        return f"\t{self.s}"


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


def AsmFormatter(f):
    def g(*args, **kwargs):
        instructions = f(*args, *kwargs)
        return [AsmInstruction(x) for x in instructions]
    return g


@AsmFormatter
def push_im(val):
    return [f"addi sp, sp, -{INT_BYTES}", f"li t1, {val}", f"sw t1, 0(sp)"]

@AsmFormatter
def push_reg(reg):
    return [f"addi sp, sp, -{INT_BYRES}", f"sw {reg}, 0(sp)"]


@AsmFormatter
def pop_reg(reg):
    return [f"lw {reg}, 0(sp)", f"addi sp, sp, {INT_BYTES}"]  # use `ld` for 64 bit

@AsmFormatter
def pop():
    return [f"addi sp, sp, {INT_BYTES}"]

@AsmFormatter
def loadTop(reg):
    return [f"lw {reg}, 0(sp)"]

@AsmFormatter
def saveTop(reg):
    return [f"sw {reg}, 0(sp)"]

@AsmFormatter
def _unary(op, reg):
    return [f"{op} {reg}, {reg}"]

def unary(op):
    return loadTop("t1") + _unary(op, "t1") + saveTop("t1")

def binary(op):
    if op in oneInsBinaryList:
        return one_binary(op)
    elif op in ['slet', 'sget']:
        return releq_binary(op)
    elif op in ['eq', 'ne']:
        return eqne_binary(op)
    elif op == 'lor':
        return lor()
    elif op == 'land':
        return land()

@AsmFormatter
def one_binary(op, reg1="t1", reg2="t2"):
    return [
        f"lw {reg1}, {INT_BYTES}(sp)",
        f"lw {reg2}, 0(sp)",
        f"{op} {reg1}, {reg1}, {reg2}",
        f"addi sp, sp, {INT_BYTES}",
        f"sw {reg1}, 0(sp)"
    ]

@AsmFormatter
def releq_binary(op):
    op_map = {'slet': 'sgt', 'sget': 'slt'}
    return [
        f"lw t1, {INT_BYTES}(sp)",
        f"lw t2, 0(sp)",
        f"{op_map[op]} t1, t1, t2",
        f"seqz t1, t1",
        f"addi sp, sp, {INT_BYTES}",
        f"sw t1, 0(sp)"
    ]
    
@AsmFormatter
def eqne_binary(op):
    op_map = {'eq': 'seqz', "ne": 'snez'}
    return [
        f"lw t1, {INT_BYTES}(sp)",
        f"lw t2, 0(sp)",
        f"sub t1, t1, t2",
        f"{op_map[op]} t1, t1",
        f"addi sp, sp, {INT_BYTES}",
        f"sw t1, 0(sp)"
    ]

@AsmFormatter
def lor():
    return [
        f"lw t1, {INT_BYTES}(sp)",
        f"lw t2, 0(sp)",
        f"or t1, t1, t2",
        f"snez t1, t1",
        f"addi sp, sp, {INT_BYTES}",
        f"sw t1, 0(sp)"
    ]

@AsmFormatter
def land():
    return [
        f"lw t1, {INT_BYTES}(sp)",
        f"lw t2, 0(sp)",
        f"snez t1, t1",
        f"snez t2, t2",
        f"and t1, t1, t2",
        f"addi sp, sp, {INT_BYTES}",
        f"sw t1, 0(sp)"
    ]

from typing import List
class AsmGenerator:
    def __init__(self, outfile:str):
        self.fout = open(outfile, 'w')
        self.typeFuncMap = { 
            IrRet: self.genRet,
            IrConst: self.genConst,
            IrUnary: self.genUnary,
            IrBinary: self.genBinary,
        }
        
    def close(self):
        self.fout.close()
        
    def printCommandList(self, commands: List[AsmInstruction]):
        for command in commands:
            print(f"{command}", file=self.fout)

    def genRet(self, instruction:IrRet):
        self.printCommandList(pop_reg("a0"))

    def genConst(self, instruction:IrConst):
        self.printCommandList(push_im(instruction.v))
    
    def genUnary(self, instruction:IrUnary):
        self.printCommandList(unary(instruction.op))
    
    def genBinary(self, instruction:IrBinary):
        self.printCommandList(binary(instruction.op))
    
    def genProgBegin(self):
        self.printCommandList(
            [
                AsmDirective(".text"),
                AsmDirective(".globl main"),
                # AsmDirective(".align	2")
                AsmLabel("main"),
            ]
        )
    
    def genProgBody(self, ir_visitor:StackIRVisitor):
        for instrcution in ir_visitor.ir_instructions:
            self.typeFuncMap[type(instrcution)](instrcution)
        
    def genProgEnd(self):
        self.printCommandList(
            [AsmInstruction("jr ra")]
        )

    def generate(self, ir_visitor):
        print(ir_visitor.getIR())
        self.genProgBegin()
        self.genProgBody(ir_visitor)
        self.genProgEnd()


def parseArgs():
    parser = argparse.ArgumentParser(description='Minidecaf compiler step 1')
    parser.add_argument("infile", type=str, help='the inpue C file')
    parser.add_argument("outfile", type=str, default='a.out', help='the output .asm file')
    return parser.parse_args()

def Lexer(inputStream):
    lexer = ExprLexer(inputStream)
    return CommonTokenStream(lexer)

def Parser(tokenStream):
    parser = ExprParser(tokenStream)
    parser._errHandler = BailErrorStrategy()
    tree = parser.program()
    print("Print Tree:")
    print(tree.toStringTree(recog=parser))
    return tree

def irGenerator(tree):
    visitor = StackIRVisitor()
    visitor.visit(tree)
    return visitor


def asmGenerator(ir_visitor, outfile):
    asm_generator = AsmGenerator(outfile=outfile)
    asm_generator.generate(ir_visitor)
    asm_generator.close()

def main():
    args = parseArgs()
    print("in dir: " + os.path.abspath('.'))
    inputStream = FileStream(args.infile)
    print(inputStream)
    tokenStream = Lexer(inputStream)
    tree = Parser(tokenStream)
    ir_visitor = irGenerator(tree)
    asmGenerator(ir_visitor, args.outfile)

