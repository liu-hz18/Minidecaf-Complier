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
Comma  : ',';
Semicolon : ';';

Punctuator :
    Lparen | Rparen | Lbrace | Rbrace | Semicolon | Comma
    ;

fragment IdentLead : [a-zA-Z_];
fragment WhitespaceChar : [ \t\n\r];
fragment Digit : [0-9];
fragment WordChar : [0-9a-zA-Z_];

Whitespace : WhitespaceChar+ -> skip ;
Integer : Digit+ ;
Identifier : IdentLead WordChar* ;
