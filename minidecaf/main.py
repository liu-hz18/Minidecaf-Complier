"""实例：真·main"""
import sys
import os
import argparse
from antlr4 import *

from .generated.ExprLexer import ExprLexer
from .generated.ExprParser import ExprParser
from .ir.visitor import StackIRVisitor, NameVisitor
from .asm.asm_gen import AsmGenerator


def parseArgs():
    parser = argparse.ArgumentParser(description='Minidecaf compiler step 1')
    parser.add_argument("infile", type=str, help='the inpue C file')
    parser.add_argument("--outfile", type=str, default=None, required=False, help='the output .asm file')
    return parser.parse_args()

def Lexer(inputStream):
    lexer = ExprLexer(inputStream)
    return CommonTokenStream(lexer)

def Parser(tokenStream):
    parser = ExprParser(tokenStream)
    parser._errHandler = BailErrorStrategy()
    tree = parser.program()
    #print("Print Tree:")
    #print(tree.toStringTree(recog=parser))
    return tree

def nameScanner(tree):
    nameVisitor = NameVisitor()
    nameVisitor.visit(tree)
    nameInfo = nameVisitor.nameInfo
    return nameInfo

def irScanner(tree, nameInfo):
    visitor = StackIRVisitor(nameInfo)
    visitor.visit(tree)
    return visitor

def asmScanner(ir_visitor, outfile=None):
    asm_generator = AsmGenerator(outfile=outfile)
    asm_generator.generate(ir_visitor)
    asm_generator.close()

def main():
    args = parseArgs()
    #print("in dir: " + os.path.abspath('.'))
    inputStream = FileStream(args.infile)
    #print(inputStream)
    tokenStream = Lexer(inputStream)
    tree = Parser(tokenStream)
    nameInfo = nameScanner(tree)
    #print(nameInfo.var)
    #print(nameInfo.funcs)
    ir_visitor = irScanner(tree, nameInfo)
    asmScanner(ir_visitor, args.outfile)
    

