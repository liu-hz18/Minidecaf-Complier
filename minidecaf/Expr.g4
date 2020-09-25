// antlr4pyvi ./Expr.g4
grammar Expr;

import ExprLex;

program: func EOF;

func: tp 'main' '(' ')' '{' statement '}';

tp: 'int';

statement: 'return' expr ';';

//expr: Integer;  //step1

expr: unary;

unary
    : Integer           # atomInteger
    | UnOperator unary  # opAndUnary
    ;
