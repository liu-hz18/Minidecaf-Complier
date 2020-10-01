INT_BYTES = 4
MAX_INT = 2**(INT_BYTES*8-1)
#MIN_INT = -2**(INT_BYTES*8)
MIN_INT = 0
unAryMap = {
    '~': 'not',
    '!': 'seqz',
    '-': 'neg',
    '&': 'addrof',
    '*': 'deref'
}
binaryMap = {
    '+': 'add',
    '-': 'sub',
    '*': 'mul',
    '/': 'div',
    '%': 'rem',
    '<': 'slt',
    '>': 'sgt',
    '<=': 'slet',
    '>=': 'sget',
    '==': 'eq',
    '!=': 'ne',
    '&&': 'land',
    '||': 'lor',
}
oneInsBinaryList = [
    'add',
    'sub',
    'mul',
    'div',
    'rem',
    'slt',
    'sgt',
]
branchOps = [
    'br',
    'beqz',
    'bnez',
    #'beq',
    #'bne',
]