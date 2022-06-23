class InvalidNumberError(Exception):
    def __init__(self, message="The number you have entered is invalid."):
        self.message = message

        super().__init__(self.message)

class InvalidToken(Exception):
    def __init__(self, token, message="The token {} is invalid"):
        self.message = message.format(token)

        super().__init__(self.message)

class NamingError(Exception):
    pass

class DeclarationError(Exception):
    pass

class ScopeError(Exception):
    pass

class UndefinedError(Exception):
    pass