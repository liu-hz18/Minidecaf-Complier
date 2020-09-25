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
    '-': 'neg'
}


class IrBaseInstraction():
    def __repr__(self):
        return self.__str__()


class IrConst(IrBaseInstraction):
    def __init__(self, v:int):
        assert MIN_INT < v < MAX_INT
        self.v = v

    def __str__(self):
        return f"const {self.v}"


class IrRet(IrBaseInstraction):
    def __str__(self):
        return f"ret"


class IrUnary(IrBaseInstraction):
    def __init__(self, op):
        assert op in unAryMap
        self.op = unAryMap[op]
    
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
    
    @overrides
    def visitOpAndUnary(self, ctx:ExprParser.OpAndUnaryContext):
        op = str(ctx.UnOperator().getText())
        self.visitChildren(ctx)
        self.ir_instructions.append(IrUnary(op))
        
        
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


from typing import List
class AsmGenerator:
    def __init__(self, outfile:str):
        self.fout = open(outfile, 'w')
        self.typeFuncMap = { 
            IrRet: self.genRet,
            IrConst: self.genConst,
            IrUnary: self.genUnary,
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
#    print("""\
#            .text
#            .globl  main
#    main:
#            li      a0,123
#            ret\
#    """)

    args = parseArgs()
    print("in dir: " + os.path.abspath('.'))
    inputStream = FileStream(args.infile)
    print(inputStream)
    tokenStream = Lexer(inputStream)
    tree = Parser(tokenStream)
    ir_visitor = irGenerator(tree)
    asmGenerator(ir_visitor, args.outfile)


# python -m minidecaf ./input.c ./input.s
# rgcc32 input.s
# file a.out
# qemu-riscv32 a.out
# echo $?
