class Token:
    def __init__(self, _type, value):
        self.type = _type
        self.value = value

    def __repr__(self):
        return f"{self.type}:{self.value}"

# A list of tokens used in the language.

STRING = "STRING" #
NUMBER = "NUMBER" #
IDENTIFIER = "IDENTIFIER" #
KEYWORD = "KEYWORD"
OPEN_BRACE = "OPEN_BRACE" #
CLOSE_BRACE = "CLOSE_BRACE" #
OPEN_PAREN = "OPEN_PAREN" #
CLOSE_PAREN = "CLOSE_PAREN" #
ASSIGNMENT = "ASSIGNMENT" #
COMMA = "COMMA" #
SEMICOLON = "SEMICOLON"
PLUS = "PLUS" #
MINUS = "MINUS" #
MULTIPLY = "MULTIPLY" #
DIVIDE = "DIVIDE" #
MODULO = "MODULO" #
COMPARISON = "COMPARISON" #
AND = "AND" #
OR = "OR" #
NOT = "NOT" #
AT = "AT" #
BOOLEAN = "BOOLEAN" #
NULL = "NULL" #
INCREMENT = "INCREMENT" #
DECREMENT = "DECREMENT" #
INCREMENT_BY = "INCREMENT_BY" #
DECREMENT_BY = "DECREMENT_BY" #
MULTIPLY_BY = "MULTIPLY_BY" #
DIVIDE_BY = "DIVIDE_BY" #
MODULO_BY = "MODULO_BY" #
OPEN_SQUARE = "OPEN_SQUARE" #
CLOSE_SQUARE = "CLOSE_SQUARE" #
LESS_THAN = "LESS_THAN" #
GREATER_THAN = "GREATER_THAN" #

# Just for the compiler

SHADOW = "SHADOW" #
SUBSTACK = "SUBSTACK" #