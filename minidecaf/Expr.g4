// antlr4pyvi ./Expr.g4
grammar Expr;

import ExprLex;

program: func EOF;

func
    : tp Identifier '(' ')' block   # funcDefine
    | tp Identifier '(' ')' ';'     # funcDeclare
    ;

tp: 'int';

block
    : '{' blockitem* '}'
    ;

blockitem
    : statement           # SingleStatement
    | declaration         # DeclareStatement
    ;


statement
    : 'return' expr ';'   # RetStatement
    | expr? ';'           # ExprStatement
    | block               # BlockStatement
    | 'if' '(' expr ')' thens=statement ('else' elses=statement)? # IfStatement         
    ;

declaration
    : tp Identifier ('=' expr)? ';'
    ;

expr: assignment;

assignment
    : conditional                     # SingleAssign
    | unary '=' expr             # ComplexAssign
    ;

conditional
    : logicalOr                             # SingleCond
    | logicalOr '?' expr ':' conditional    # ComplexCond
    ;

logicalOr
    : logicalAnd                    # SingleOr
    | logicalOr '||' logicalAnd     # ComplexOr
    ;

logicalAnd
    : equality                    # SingleAnd
    | logicalAnd '&&' equality        # ComplexAnd
    ;

equality
    : relational                    # SingleEq
    | equality eqOperator relational # ComplexEq
    ;

relational
    : additive                      # SingleRe
    | relational relOperator additive  # ComplexRe
    ;

additive
    : multiplicative                        # SingleAdd
    | additive addOperator multiplicative   # ComplexAdd
    ;

multiplicative
    : unary                                 # SingleMul
    | multiplicative mulOperator unary      # ComplexMul
    ;

unary
    : primary             # SingleUnary
    | unOperator unary    # ComplexUnary
    ;

primary
    : Integer       # atomInteger
    | '(' expr ')'  # ComplexPrimary
    | Identifier    # atomIdentifier
    ;

// un-op
unOperator: 
    '-' | '~' | '!'
    ;

// bi-op
addOperator
    : '+' | '-'
    ;

mulOperator
    : '*' | '/' | '%'
    ;

eqOperator
    : '==' | '!='
    ;

relOperator
    : '<' | '>' | '<=' | '>='
    ; 