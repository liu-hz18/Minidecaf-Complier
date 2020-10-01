import copy
from ..utils import INT_BYTES

class Type():
    def __repr__(self):
        return self.__str__()
    
    def __eq__(self, other):
        return self.__str__() == other.__str__()

class IntType(Type):
    def __str__(self):
        return "int"
    
    def sizeof(self):
        return INT_BYTES
    
class PointerType(Type):
    def __init__(self, base:Type):
        self.base = base
        
    def __str__(self):
        return f"{self.base}*"

    def __eq__(self, other):
        if not isinstance(other, PointerType):
            return False
        return self.base == other.base

    def sizeof(self):
        return INT_BYTES
    
class OneDimArrayType(Type):
    def __init__(self, base:Type, length:int):
        self.base = base
        self.length = length
        self.ndims = 1
        
    def __str__(self):
        return f"{self.base}[{self.length}]"
    
    def __eq__(self, other):
        if not isinstance(other, OneDimArrayType):
            return False
        return self.base == other.base and self.length == other.length
    
    def sizeof(self):
        return self.base.sizeof() * self.length

class ArrayType(Type):
    def __init__(self, base:Type, len_list:list):
        self.item_type = base
        self.ndims = len(len_list)
        self.len_list = len_list
        _base = base
        self.size = 1
        for dim_len in len_list:
            _base = OneDimArrayType(_base, dim_len)
            self.size *= dim_len
        self.base = _base
        self.size *= base.sizeof()
        
    def unwarp(self):
        return self.base
    
    def __str__(self):
        return f"{self.base}[{self.length}]"
        
    def sizeof(self):
        return self.size
