
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
