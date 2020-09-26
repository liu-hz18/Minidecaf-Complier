from typing import List

from ..ir.ir_instructions import *
from ..ir.visitor import StackIRVisitor
from .asm_instructions import *
from .asm_format import *

class AsmGenerator:
    def __init__(self, outfile:str):
        self.fout = open(outfile, 'w')
        self._curFuncName = None
        self.typeFuncMap = { 
            IrRet: self.genRet,
            IrConst: self.genConst,
            IrUnary: self.genUnary,
            IrBinary: self.genBinary,
            IrStore: self.genStore,
            IrLoad: self.genLoad,
            IrPop: self.genPop,
            IrFrameAddr: self.genFrameAddr,
            # IrFunction: self.genFunction,
        }
        
    def close(self):
        self.fout.close()
        
    def printCommandList(self, commands: List[AsmInstruction]):
        for command in commands:
            print(f"{command}", file=self.fout)

    def genRet(self, instruction:IrRet):
        self.printCommandList(ret(self._curFuncName))

    def genConst(self, instruction:IrConst):
        self.printCommandList([AsmComment(f"push {instruction.v}")] + push_im(instruction.v))
    
    def genUnary(self, instruction:IrUnary):
        self.printCommandList([AsmComment(instruction.op)] + unary(instruction.op))
    
    def genBinary(self, instruction:IrBinary):
        self.printCommandList([AsmComment(instruction.op)] + binary(instruction.op))
    
    def genLoad(self, instruction:IrLoad):
        self.printCommandList([AsmComment("load *(addr = top) to top")] + load())
    
    def genStore(self, instruction:IrStore):
        self.printCommandList([AsmComment("store 4(sp) to *(addr = top)")] + store())
        
    def genFrameAddr(self, instruction:IrFrameAddr):
        self.printCommandList([AsmComment(f"push addr = {instruction.offset}(fp)")] + frameaddr(instruction.offset))
    
    def genPop(self, instruction:IrPop):
        self.printCommandList([AsmComment("pop stack")] + pop())
    
    def _genPrologue(self, instruction:IrFunction):
        self.printCommandList(
            [
                AsmBlank(),
                AsmDirective(".text"),
                AsmDirective(f".globl {instruction.name}"),
                AsmLabel(f"{instruction.name}"),
                AsmComment("prologue"),
                *push_reg("ra"),
                *push_reg("fp"),
                AsmInstruction("mv fp, sp"),
            ]
        )
        for i in range(instruction.nParams):
            self.printCommandList([
                AsmInstruction(f"lw t1, {INT_BYTES*(i+2)}(fp)"),
                *push_reg("t1"),
            ])
    
    def _genEpilogue(self, instruction:IrFunction):
        self.printCommandList([
            AsmBlank(),
            AsmComment("set default `stack top` = 0"),
            *push_im(0),
            AsmLabel(f"{instruction.name}_exit"),
            AsmComment("epilogue"),
            AsmInstruction(f"lw a0, 0(sp)"),
            AsmInstruction(f"mv sp, fp"),
            *pop_reg("fp"),
            *pop_reg("ra"),
            AsmInstruction("jr ra"),
            AsmBlank()
        ])
    
    def genFunction(self, instruction:IrFunction):
        self._curFuncName = instruction.name
        self._genPrologue(instruction)
        for instr in instruction.instr:
            self.printCommandList([AsmBlank()])
            self.typeFuncMap[type(instr)](instr)
        self._genEpilogue(instruction)
    
    def genProgBegin(self):
        self.printCommandList(
            [
                AsmDirective(".text"),
                AsmDirective(".globl main"),
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
        for function in ir_visitor.funcs:
            self.genFunction(function)
