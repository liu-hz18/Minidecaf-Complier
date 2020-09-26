from typing import List
from ..utils import *

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

class IrPop(IrBaseInstraction):
    def __str__(self):
        return "pop"
    
class IrLoad(IrBaseInstraction):
    def __str__(self):
        return "load"
    
class IrStore(IrBaseInstraction):
    def __str__(self):
        return "store"

class IrFrameAddr(IrBaseInstraction):
    def __init__(self, offset:int):
        assert offset < 0
        self.offset = offset

    def __str__(self):
        return f"frameaddr {self.offset}"

class IrFunction(IrBaseInstraction):
    def __init__(self, name:str, nParams:int, instructions:List[IrBaseInstraction]):
        self.name = name
        self.nParams = nParams
        self.instr = instructions
    
    def __str__(self):
        body = '\n\t'.join(self.instr)
        return f"{self.name}({self.nParams}):\n{body}"

class IrGlobalSymbol(IrBaseInstraction):
    def __init__(self, symbol:str):
        self.symbol = symbol
    
    def __str_(self):
        return f"globalsymbol {self.symbol}"
   
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
        return f"{self.op} {self.label}"
