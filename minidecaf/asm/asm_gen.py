from typing import List

from ..ir.ir_instructions import *
from ..ir.visitor import StackIRVisitor
from .asm_instructions import *
from .asm_format import *

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
