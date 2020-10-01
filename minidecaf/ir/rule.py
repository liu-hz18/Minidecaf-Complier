from .type import *

def opBinaryAddRule(left, right):
    err = []
    try:
        return opBinaryRule(left, right)
    except Exception as e:
        err.append(str(e))
    try:
        return pointerAddRule(left, right)
    except Exception as e:
        err.append(str(e))
    raise Exception('\n'.join(err))
    
def opBinarySubRule(left, right):
    err = []
    try:
        return opBinaryRule(left, right)
    except Exception as e:
        err.append(str(e))
    try:
        return pointerAddRule(left, right)
    except Exception as e:
        err.append(str(e))
    try:
        return pointerDiffRule(left, right)
    except Exception as e:
        err.append(str(e))
    raise Exception('\n'.join(err))

def opBinaryRule(left, right):
    if isinstance(left, IntType) and isinstance(right, IntType):
        return IntType()
    else:
        raise Exception(f"`int` expected, got <{left}> and <{right}>.")

def pointerAddRule(left, right):
    if isinstance(left, IntType) and isinstance(right, PointerType):
        return right
    if isinstance(right, IntType) and isinstance(left, PointerType):
        return left
    raise Exception(f"`ptr` and `int` expected, found {left}")

def pointerDiffRule(left, right):
    if isinstance(left, PointerType) and isinstance(right, PointerType) and isinstance(left.base, type(right.base)):
        return IntType()
    raise Exception(f"two ptrs should be the same type, found <{left}> and `{right}`")

def opUnaryRule(left):
    if isinstance(left, IntType):
        return IntType()
    else:
        raise Exception(f"`int` expected, got <{left}> and <{right}>.")
    
def opDerefRule(left):
    if isinstance(left, PointerType):
        return left.base
    else:
        raise Exception(f"`ptr` expected, got <{left}>")
    
def opAddrOfRule(left):
    if isinstance(left, OneDimArrayType):
        raise Exception("cannot get address of an array")
    return PointerType(left)

def opEqRule(left, right):
    if left != right:
        raise Exception(f"cannot compare {left} to {right}")
    if isinstance(left, IntType) or isinstance(left, PointerType):
        return IntType()
    else:
        raise Exception(f"expected `int` or `ptr`, found {left}")
    
def opRelRule(left, right):
    if isinstance(left, IntType) and isinstance(right, IntType):
        return IntType()
    raise Exception("`int` expected for Relational Operator")
    
    
def opAssignRule(left, right):
    import sys
    if left != right:
        raise Exception(f"cannot assign <{right}> to lvalue:{left}")
    if isinstance(left, OneDimArrayType):
        raise Exception(f"cannot assign <{right}> to Array Type")
    return left

def arrayIndexRule(arr, index):
    if not isinstance(arr, OneDimArrayType) and not isinstance(arr, PointerType):
        raise Exception(f"array or ptr expected, {arr} found")
    if isinstance(index, IntType):
        return arr.base
    else:
        raise Exception(f"index must be `int`, found {index}")

def intRule(left):
    if not isinstance(left, IntType):
        raise Exception("`int` expected, found {left}")
    
def returnRule(func_ret_type, value_type):
    if not isinstance(func_ret_type, type(value_type)):
        raise Exception(f"return type {func_ret_type} expected, found {value_type}")

def conditionRule(condition, then, _else):
    if isinstance(condition, IntType) and isinstance(then, type(_else)):
        return then


ruleBinaryFuncMap = {
    '*': opBinaryRule,
    '/': opBinaryRule,
    '%': opBinaryRule,
    '&&': opBinaryRule,
    '||': opBinaryRule,
    
    '=': opAssignRule,
    
    '+': opBinaryAddRule,
    '-': opBinarySubRule,
    
    '==': opEqRule,
    '!=': opEqRule,
    '>': opRelRule,
    '<': opRelRule,
    '>=': opRelRule,
    '<=': opRelRule,
}

ruleUnaryFuncMap = {
    '-': opUnaryRule,
    '!': opUnaryRule,
    '~': opUnaryRule,
    
    '&': opAddrOfRule,
    '*': opDerefRule,
}