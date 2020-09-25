INT_BYTES = 4
MAX_INT = 2**(INT_BYTES*8-1) - 1
#MIN_INT = -2**(INT_BYTES*8)
MIN_INT = 0
unAryMap = {
    '~': 'not',
    '!': 'seqz',
    '-': 'neg',
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
