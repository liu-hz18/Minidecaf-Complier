"""实例：真·main"""
import sys
import os
import argparse
from antlr4 import *

from .generated.ExprLexer import ExprLexer
from .generated.ExprParser import ExprParser
from .ir.visitor import StackIRVisitor
from .ir.type_visitor import TypeVisitor
from .ir.name_visitor import NameVisitor
from .asm.asm_gen import AsmGenerator
from .ir.info import NameInfo, TypeInfo


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
    return tree

def nameScanner(tree):
    nameVisitor = NameVisitor()
    nameVisitor.visit(tree)
    nameInfo = nameVisitor.nameInfo
    return nameInfo

def typeScanner(tree, nameInfo):
    typeVisitor = TypeVisitor(nameInfo)
    typeVisitor.visit(tree)
    typeInfo = typeVisitor.type_info
    return typeInfo

def irScanner(tree, nameInfo, typeInfo):
    visitor = StackIRVisitor(nameInfo, typeInfo)
    visitor.visit(tree)
    return visitor

def asmScanner(ir_visitor, outfile=None):
    asm_generator = AsmGenerator(outfile=outfile)
    asm_generator.generate(ir_visitor)
    asm_generator.close()

def main():
    args = parseArgs()
    inputStream = FileStream(args.infile)
    tokenStream = Lexer(inputStream)
    tree = Parser(tokenStream)
    nameInfo = nameScanner(tree)
    typeInfo = typeScanner(tree, nameInfo)
    ir_visitor = irScanner(tree, nameInfo, typeInfo)
    asmScanner(ir_visitor, args.outfile)
