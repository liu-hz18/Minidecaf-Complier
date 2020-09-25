
from .asm_instructions import AsmInstruction
from ..utils import *

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
