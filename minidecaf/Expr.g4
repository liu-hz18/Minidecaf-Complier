// antlr4pyvi ./Expr.g4
grammar Expr;

import ExprLex;

program: func EOF;

func: tp 'main' '(' ')' '{' statement '}';

tp: 'int';

statement: 'return' expr ';';

expr: logicalOr;

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