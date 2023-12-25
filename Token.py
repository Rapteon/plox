from TokenType import TokenType


class Token:
    def __init__(self, tokenType: TokenType, lexeme: str, literal, line: int):
       self.type = tokenType
       self.lexeme = lexeme
       self.literal = literal
       self.line = line
       
    def __repr__(self):
        return self.type + " " + self.lexeme + " " + self.literal
    
    """
    @TODO
    fix printing of TokenTypes
    figure out how to print enums
    how to print literals if the value is None
    """