lexer grammar ExprLex;
// keyword
Int 
    : 'int'
    ;
Return
    : 'return'
    ;

// punc
Lparen : '(';
Rparen : ')';
Lbrace : '{';
Rbrace : '}';
Semicolon : ';';

Punctuator :
    Lparen | Rparen | Lbrace | Rbrace | Semicolon
    ;

UnOperator: 
    '-' | '~' | '!'
    ;

// bi-op
Add : '+';
Sub : '-';
Mul : '*';
Div : '/';
Mod : '%';

BiOperator :
    Add | Sub | Mul | Div | Mod
    ;

fragment WhitespaceChar : [ \t\n\r];
fragment Digit : [0-9];
fragment WordChar : [0-9a-zA-Z];

Whitespace : WhitespaceChar+ -> skip;
Integer : Digit+;
