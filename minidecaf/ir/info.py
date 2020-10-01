

class NameInfo():
    def __init__(self):
        self.var = {}
        self.funcs = {}
        self.globals = {}

    def freeze(self):
        for funcNameInfo in self.funcs.values():
            self.var.update(funcNameInfo.var)

    def __getitem__(self, ctx):
        return self.var[ctx]

    def __str__(self):
        return "\tvar: " + str(self.var) + "\n\tfuncs: " + str(self.funcs) + "\n\tglobals: " + str(self.globals)

    def __repr__(self):
        return self.__str__()


class FuncNameInfo():
    def __init__(self, hasDef=True):
        self.var = {}
        self.pos = {}
        self.blockSlots = {}
        self.hasDef = hasDef

    def bind(self, varstr, var, pos):
        self.var[varstr] = var
        self.pos[varstr] = pos

    def __str__(self):
        return str(self.var) + str(self.hasDef)

    def __repr__(self):
        return self.__str__()

    def __getitem__(self, varstr):
        return self.var[varstr]
    
class TypeInfo():
    def __init__(self):
        self.ctx_type = {}
        self.ctx_location = {}
        self.func_ret_type = {}
        self.func_param_type = {}
        
    def getLvalueLocation(self, ctx):
        return self.ctx_location[ctx]
    
    def setLvalueLocation(self, ctx, loc:list):
        self.ctx_location[ctx] = loc
        
    def __getitem__(self, ctx):
        return self.ctx_type[ctx]
    
    def __setitem__(self, ctx, tp):
        self.ctx_type[ctx] = tp
        
    def __str__(self):
        return "\tctx_type: " + str(self.ctx_type) + "\n\tctx_location: " + str(self.ctx_location)
