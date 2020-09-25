class AsmBase():
    def __init__(self, s):
        self.s = s

    def __repr__(self):
        return self.__str__()

class AsmInstruction(AsmBase):
    def __str__(self):
        return f"\t{self.s}"

class AsmLabel(AsmBase):
    def __str__(self):
        return f"{self.s}:"
    
class AsmComment(AsmBase):
    def __str__(self):
        return f"\t#{self.s}"
    
class AsmDirective(AsmBase):
    def __str__(self):
        return f"\t{self.s}"
