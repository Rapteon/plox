from TokenType import TokenType


class Token:
    def __init__(self, tokenType: TokenType, lexeme: str, literal, line: int):
       self.type = tokenType
       self.lexeme = lexeme
       self.literal = literal
       self.line = line
       
    def __repr__(self):
        if self.literal == None:
            return self.type.name + " " + self.lexeme
        
        return self.type.name + " " + self.lexeme + " " + self.literal
 