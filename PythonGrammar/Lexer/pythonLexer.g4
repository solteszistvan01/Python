//https://github.com/antlr/grammars-v4/blob/master/python/python3-py/Python3.g4
//


lexer grammar pythonLexer;

STRING:;

NUMBER:;

INTEGER:;

DEF:;
RETURN:;
RAISE:;
FROM:;
IMPORT:;
AS:;
GLOBAL:;
NONLOCAL:;
ASSERT:;
IF:;
ELIF:;
ELSE:;
WHILE:;
FOR:;
IN:;
TRY:;
FINALLY:;
WITH:;
EXCEPT:;
LAMBDA:;
OR:;
AND:;
NOT:;
IS:;
NONE:;
TRUE:;
FALSE:;
CLASS:;
YIELD:;
DEL:;
PASS:;
CONTINUE:;
BREAK:;
ASYNC:;
AWAIT:;

NEWLINE:;

NAME:;

STRING_LITERAL:;

BYTES_LITERL:;

DECIMAL_INTEGER:;

OCT_INTEGER:;

HEX_INTEGER:;

BIN_INTEGER:;

FLOAT_NUMBER:;

IMAG_NUMBER:;

DOT:;
ELLIPSIS:;
STAR:;
OPEN_PAREN:;
CLOSE_PAREN:;
COMMA:;
COLON:;
SEMI_COLON : ';';
POWER : '**';
ASSIGN : '=';
OPEN_BRACK:;
CLOSE_BRACK:;
OR_OP : '|';
XOR : '^';
AND_OP : '&';
LEFT_SHIFT : '<<';
RIGHT_SHIFT : '>>';
ADD : '+';
MINUS : '-';
DIV : '/';
MOD : '%';
IDIV : '//';
NOT_OP : '~';
OPEN_BRACE:;
CLOSE_BRACE:;
LESS_THAN : '<';
GREATER_THAN : '>';
EQUALS : '==';
GT_EQ : '>=';
LT_EQ : '<=';
NOT_EQ_1 : '<>';
NOT_EQ_2 : '!=';
AT : '@';
ARROW : '->';
ADD_ASSIGN : '+=';
SUB_ASSIGN : '-=';
MULT_ASSIGN : '*=';
AT_ASSIGN : '@=';
DIV_ASSIGN : '/=';
MOD_ASSIGN : '%=';
AND_ASSIGN : '&=';
OR_ASSIGN : '|=';
XOR_ASSIGN : '^=';
LEFT_SHIFT_ASSIGN : '<<=';
RIGHT_SHIFT_ASSIGN : '>>=';
POWER_ASSIGN : '**=';
IDIV_ASSIGN : '//=';

SKIP_ : ;

UNKNOWN_CHAR:;

//TODO:Fragments and the difference between fragmented and non fragmented keywords!