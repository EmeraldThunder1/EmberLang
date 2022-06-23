from src.tokens import *
from src.errors import *

class Lexer:
    def __init__(self):
        self.idx = 0
        self.tokens = []
        self.code = None

    def lex(self, code):
        self.tokens = []
        self.code = code

        code[0]
        while self.idx < len(code):
            if code[self.idx] in " \n\t":
                self.idx += 1  # Character is whitespace
            elif code[self.idx] == "#":
                while self.idx < len(code) - 1 and code[self.idx] != "\n":
                    self.idx += 1
            elif code[self.idx] in ["'", '"']:
                self.tokens.append(Token(STRING, self.get_string()))
            elif code[self.idx] in "0123456789":
                self.tokens.append(Token(NUMBER, self.get_number()))
            elif code[self.idx].isalpha() or code[self.idx] == "_":
                identifier = self.get_identifier()

                _type = IDENTIFIER

                if identifier == "true" or identifier == "false":
                    _type = BOOLEAN
                elif identifier == "null":
                    _type = NULL

                self.tokens.append(Token(_type, identifier))

            elif code[self.idx] == "{":
                self.save_token(OPEN_BRACE, "{")
            elif code[self.idx] == "}":
                self.save_token(CLOSE_BRACE, "}")
            elif code[self.idx] == "(":
                self.save_token(OPEN_PAREN, "(")
            elif code[self.idx] == ")":
                self.save_token(CLOSE_PAREN, ")")
            elif code[self.idx] == "[":
                self.save_token(OPEN_SQUARE, "[")
            elif code[self.idx] == "]":
                self.save_token(CLOSE_SQUARE, "]")
            elif code[self.idx] == "=":

                if self.idx < len(code) - 1 and code[self.idx + 1] == "=":
                    self.save_token(COMPARISON, "==")
                    self.idx += 1
                else:
                    self.save_token(ASSIGNMENT, "=")
            elif code[self.idx] == ",":
                self.save_token(COMMA, ",")
            elif code[self.idx] == ";":
                self.save_token(SEMICOLON, ";")
            elif code[self.idx] == "+":
                after = None
                if self.idx < len(code) - 1:
                    after = code[self.idx + 1]
                
                if after == '+':
                    self.save_token(INCREMENT, "++")
                    self.idx += 1
                elif after == '=':
                    self.save_token(INCREMENT_BY, "+=")
                    self.idx += 1
                else:
                    self.save_token(PLUS, "+")

            elif code[self.idx] == "-":
                after = None
                if self.idx < len(code) - 1:
                    after = code[self.idx + 1]
                
                if after == '-':
                    self.save_token(DECREMENT, "--")
                    self.idx += 1
                elif after == '=':
                    self.save_token(DECREMENT_BY, "-=")
                    self.idx += 1
                else:
                    self.save_token(MINUS, "-")

            elif code[self.idx] == '*':
                after = None
                if self.idx < len(code) - 1:
                    after = code[self.idx + 1]

                if after == '=':
                    self.save_token(MULTIPLY_BY, "*=")
                    self.idx += 1
                else:
                    self.save_token(MULTIPLY, "*")

            elif code[self.idx] == '/':
                after = None
                if self.idx < len(code) - 1:
                    after = code[self.idx + 1]

                if after == '=':
                    self.save_token(DIVIDE_BY, "/=")
                    self.idx += 1
                else:
                    self.save_token(DIVIDE, "/")
            
            elif code[self.idx] == '%':
                after = None
                if self.idx < len(code) - 1:
                    after = code[self.idx + 1]

                if after == '=':
                    self.save_token(MODULO_BY, "%=")
                    self.idx += 1
                else:
                    self.save_token(MODULO, "%")
            elif code[self.idx] == '!':
                self.save_token(NOT, "!")
            elif code[self.idx] == '&':
                if self.idx < len(code) - 1 and code[self.idx + 1] == '&':
                    self.save_token(AND, "&&")
                    self.idx += 1

                else:
                    raise(InvalidToken("&"))

            elif code[self.idx] == '|':
                if self.idx < len(code) - 1 and code[self.idx + 1] == '|':
                    self.save_token(OR, "||")
                    self.idx += 1

                else:
                    raise(InvalidToken("|"))

            elif code[self.idx] == '@':
                self.save_token(AT, "@")

            elif code[self.idx] == '<':
                self.save_token(LESS_THAN, "<")

            elif code[self.idx] == '>':
                self.save_token(GREATER_THAN, ">")

            else:
                raise(InvalidToken(code[self.idx]))

        return self.tokens

    def get_string(self):
        string = ""

        self.idx += 1

        while not self.code[self.idx] in ["'", '"']:
            string += self.code[self.idx]
            self.idx += 1

        self.idx += 1

        return string


    def get_number(self):
        number = ""

        dot_count = 0

        while self.idx < len(self.code) and self.code[self.idx] in ".0123456789":
            if self.code[self.idx] == ".":
                dot_count += 1

                if dot_count > 1:
                    raise(InvalidNumberError("Only one decimal point is allowed in a number"))

            number += self.code[self.idx]
            self.idx += 1

        return number

    def get_identifier(self):
        identifier = ""

        while self.idx < len(self.code) and (self.code[self.idx].isalpha() or self.code[self.idx] == "_"):
            identifier += self.code[self.idx]
            self.idx += 1

        return identifier

    def save_token(self, _type, name):
        self.tokens.append(Token(_type, name))
        self.idx += 1
