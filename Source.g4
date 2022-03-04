grammar Source;

/*
 * Parser Rules
 */

program: (line)+ EOF;

line: statement NEWLINE+;

// Statement

statement: (
    some_statement
);

some_statement: VARIABLE (SPACE VARIABLE)*;
 

// TODO - list more parser rules here

/*
 * Lexer Rules (Start with Uppercase)
 */

fragment LOWERCASE: [a-z];
fragment UPPERCASE: [A-Z];
fragment DIGIT: [0-9];

SPACE: ' ';
NEWLINE: '\n';

NUMBER: DIGIT+ ([.] DIGIT+)?;

VARIABLE: (LOWERCASE | UPPERCASE) (
    LOWERCASE 
    | UPPERCASE
    | DIGIT
)+;

// TODO - list more lexer Rules here
