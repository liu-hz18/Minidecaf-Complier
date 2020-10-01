from ..utils import INT_BYTES

class Variable():
    _var_counter = {}
    def __init__(self, identifier:str, offset:int, size:int=INT_BYTES):
        if identifier in Variable._var_counter:
            Variable._var_counter[identifier] += 1
        else:
            Variable._var_counter[identifier] = 0
        self.uid = Variable._var_counter[identifier]
        self.ident = identifier
        self.offset = offset
        self.size = size
    
    def __str__(self):
        return f"{self.ident}({self.uid}|{self.offset}|{self.size})"
    
    def __repr__(self):
        return self.__str__()

    def __hash__(self):
        return hash((self.ident, self.uid, self.offset, self.size))

    def __eq__(self, other):
        return self.uid == other.uid and self.ident == other.ident and self.offset == other.offset and self.size == other.size