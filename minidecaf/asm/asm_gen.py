from typing import List
import sys

from ..ir.ir_instructions import *
from ..ir.visitor import StackIRVisitor
from .asm_instructions import *
from .asm_format import *

class AsmGenerator:
    def __init__(self, outfile:str):
        if outfile is not None:
            self.fout = open(outfile, 'w')
        else:
            self.fout = sys.stdout
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
            IrBranch: self.genBranch,
            IrLabel: self.genLabel,
            IrCall: self.genCall,
            IrGlobalAddr: self.genGlobalSymbolUse,
            
        }
        
    def close(self):
        if self.fout is not sys.stdout:
            self.fout.close()
        
    def printCommandList(self, commands: List[AsmInstruction]):
        for command in commands:
            print(f"{command}", file=self.fout)

    def genLabel(self, instruction:IrLabel):
        self.printCommandList([AsmLabel(instruction.label)])

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
        
    def genBranch(self, instruction:IrBranch):
        if instruction.op == 'br':
            self.printCommandList([AsmComment("branch")] + br(instruction.label))
        else:
            self.printCommandList([AsmComment(f"branch on `{instruction.op}`")] + br_cond(instruction.op, instruction.label))        
           
    def genCall(self, instruction:IrCall):
        call_func = None
        for func in self.funcs:
            if func.name == instruction.label:
                call_func = func
                break
        if call_func is not None:
            self.printCommandList(call(call_func.name, call_func.nParams))
        else:
            raise Exception(f"function <{instruction.label}(...)> not declared.")

    def _genPrologue(self, instruction:IrFunction):
        self.printCommandList(
            [
                AsmComment(f"function {instruction.name}"),
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
    
    def genGlobalSymbolUse(self, instruction:IrGlobalAddr):
        self.printCommandList(globaladdr(instruction.label))
    
    def genGlobalSymbolDefine(self, instruction:IrGlobalSymbol):
        self.printCommandList([
            AsmDirective(f".globl {instruction.label}"),
            AsmDirective(f".size {instruction.label}, {instruction.size}"),
            AsmLabel(f"{instruction.label}"),
            AsmDirective(f".word {instruction.value}")
        ])
        
    def genGlobalSymbolDeclare(self, instruction:IrGlobalSymbol):
        self.printCommandList([
            AsmDirective(f".comm {instruction.label}, {instruction.size}, {INT_BYTES}")
        ])
        
    def genGlobalSymbol(self):
        self.printCommandList([
            AsmComment("global symbol definition."),
            AsmDirective(f".data"),
            AsmDirective(f".align {INT_BYTES}"),
        ])
        for glob_instr in self.glob_def:
            self.genGlobalSymbolDefine(glob_instr)
        self.printCommandList([
            AsmBlank(),
            AsmComment("global symbol declaration."),
            AsmDirective('.bss')
        ])
        for glob_instr in self.glob_dec:
            self.genGlobalSymbolDeclare(glob_instr)

    def generate(self, ir_visitor):
        # print(ir_visitor.getIR(), file=sys.stderr)
        self.glob_def = ir_visitor.glob_def
        self.glob_dec = ir_visitor.glob_dec
        self.funcs = ir_visitor.funcs
        self.printCommandList([AsmComment("Generated by MiniDecaf Complier. All rights reserved.")])
        self.genGlobalSymbol()
        self.printCommandList([
            AsmBlank(),
            AsmDirective(".text"),
        ])
        for function in self.funcs:
            self.genFunction(function)
