from typing import List
import sys
from .variable import Variable
from ..utils import *

class IrBaseInstraction():
    def __repr__(self):
        return self.__str__()


class IrConst(IrBaseInstraction):
    def __init__(self, v:int):
        assert MIN_INT <= v < MAX_INT
        self.v = v

    def __str__(self):
        return f"\tpushi {self.v}"


class IrRet(IrBaseInstraction):
    def __str__(self):
        return f"\tret"


class IrUnary(IrBaseInstraction):
    def __init__(self, op):
        assert op in unAryMap
        self.op = unAryMap[op]
    
    def __str__(self):
        return '\t' + self.op
        
class IrBinary(IrBaseInstraction):
    def __init__(self, op):
        assert op in binaryMap
        self.op = binaryMap[op]
    
    def __str__(self):
        return '\t' + self.op

class IrPop(IrBaseInstraction):
    def __str__(self):
        return "\tpop"
    
class IrLoad(IrBaseInstraction):
    def __str__(self):
        return "\tload"
    
class IrStore(IrBaseInstraction):
    def __str__(self):
        return "\tstore"

class IrFrameAddr(IrBaseInstraction):
    def __init__(self, offset:int):
        assert offset < 0
        self.offset = offset

    def __str__(self):
        return f"\tframeaddr {self.offset}"

class IrFunction(IrBaseInstraction):
    def __init__(self, name:str, nParams:int, instructions:List[IrBaseInstraction], param_type:List[str], ret_type:str):
        self.name = name
        self.nParams = nParams
        self.param_type = param_type
        self.instr = instructions
        self.ret_type = ret_type
    
    def __str__(self):
        body = '\n'.join(map(str, self.instr))
        return f"{self.name}({self.nParams}):\n{body}"
    
    def __hash__(self):
        return hash((self.name, self.nParams, ','.join(self.param_type)))
    
    def __eq__(self, other):
        return self.name == other.name and self.nParams == other.nParams and \
               self.param_type == other.param_type

class IrGlobalSymbol(IrBaseInstraction):
    def __init__(self, label:str, value:int=None, variable:Variable=None, size:int=INT_BYTES):
        self.label = label
        self.value = value
        self.variable = variable
        self.size = size
    
    def __str__(self):
        return f"globalsymbol: {self.label}={self.value}(size={self.size})"

class IrGlobalAddr(IrBaseInstraction):
    def __init__(self, label:str):
        self.label = label
    
    def __str__(self):
        return f"\tglobaladdr {self.label}"

class IrLabel(IrBaseInstraction):
    def __init__(self, label: str):
        self.label = label
    
    def __str__(self):
        return f"{self.label}:"
    
class IrBranch(IrBaseInstraction):
    def __init__(self, op, label:str):
        assert op in branchOps
        self.op = op
        self.label = label
        
    def __str__(self):
        return f"\t{self.op} {self.label}"

class IrCall(IrBaseInstraction):
    def __init__(self, label):
        self.label = label
        
    def __str__(self):
        return f"\tcall {self.label}"
