// antlr4pyvi ./Expr.g4
grammar Expr;

import ExprLex;

program: globalDeclare+ EOF;

globalDeclare
    : func          # funcGlobalDeclare
    | declaration   # symbolGlobalDeclare
    ;

func
    : tp Identifier '(' paramlist ')' block   # funcDefine
    | tp Identifier '(' paramlist ')' ';'     # funcDeclare
    ;

paramlist
    : (paramDeclare (',' paramDeclare)*)?
    ;

paramDeclare
    : tp Identifier
    ;

tp
    : 'int'         # scalar
    | tp '*'        # pointer
    ;

block
    : '{' blockitem* '}'
    ;

blockitem
    : statement           # SingleStatement
    | declaration         # DeclareStatement
    ;

statement
    : 'return' expr ';'   # RetStatement
    | expr ';'            # ExprStatement
    | ';'                 # NullStatement
    | block               # BlockStatement
    | 'if' '(' expr ')' thens=statement ('else' elses=statement)? # IfStatement     
    | 'for' '(' pre=expr? ';' cond=expr? ';' post=expr? ')' statement  # forNaiveStatement
    | 'for' '(' pre=declaration cond=expr? ';' post=expr? ')' statement  # forDeclareStatement
    | 'while' '(' expr ')' statement        # WhileStatement
    | 'do' statement 'while' '(' expr ')' ';'  # doWhileStatement
    | 'break' ';'               # BreakStatement
    | 'continue' ';'            # ContinueStatement
    ;

declaration
    : tp Identifier ('[' Integer ']')* ('=' expr)? ';'
    ;

exprlist
    : (expr (',' expr)*)?
    ;

expr: assignment;

assignment
    : conditional                     # SingleAssign
    | unary '=' expr                  # ComplexAssign
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
    | relational  additive          # ComplexRe
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
    : postfix             # SingleUnary
    | unOperator unary    # ComplexUnary
    | ('(' tp ')') unary    # Cast
    ;

postfix
    : primary                       # SinglePostfix
    | Identifier '(' exprlist ')'   # ComplexPostfix
    | postfix '[' expr ']'          # ArrayIndex
    ;

primary
    : Integer       # atomInteger
    | '(' expr ')'  # ComplexPrimary
    | Identifier    # atomIdentifier
    ;

// un-op
unOperator: 
    '-' | '~' | '!' | '&' | '*'
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