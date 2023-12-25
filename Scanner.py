from Token import Token
from TokenType import TokenType
# from Lox import error
class Scanner:
    
    start = 0
    current = 0
    line = 1
    
    def __init__(self, source: str):
        # self.source = source
        self.source = "()"
        self.tokens = []
        
    
    def scanTokens(self):
        while not self.end():
            self.start = self.current
            self.scanToken()
        
        self.tokens.append(Token(TokenType.EOF, "", None, self.line))
        print(self.tokens)
        return self.tokens
    
    def scanToken(self):
        c = self.advance()
        match c:
            case '(': 
                self.addToken(TokenType.LEFT_PAREN)
            case ')': 
                self.addToken(TokenType.RIGHT_PAREN)
            case '{': 
                self.addToken(TokenType.LEFT_BRACE) 
            case '}': 
                self.addToken(TokenType.RIGHT_BRACE) 
            case ',': 
                self.addToken(TokenType.COMMA) 
            case '.': 
                self.addToken(TokenType.DOT) 
            case '-': 
                self.addToken(TokenType.MINUS) 
            case '+': 
                self.addToken(TokenType.PLUS) 
            case ';': 
                self.addToken(TokenType.SEMICOLON) 
            case '*': 
                self.addToken(TokenType.STAR) 
            case '!':
                self.addToken(TokenType.BANG_EQUAL) if match("=") else self.addToken(TokenType.BANG)
            case '=':
                self.addToken(TokenType.EQUAL_EQUAL) if match("=") else self.addToken(TokenType.EQUAL)
            case '>':
                self.addToken(TokenType.GREATER_EQUAL) if match("=") else self.addToken(TokenType.GREATER)
            case '<':
                self.addToken(TokenType.LESS_EQUAL) if match("=") else self.addToken(TokenType.LESS)
            case '/':
                if self.match('/'):
                    while self.peek() != '\n' and not self.end():
                        self.advance()
                else:
                    self.addToken(TokenType.SLASH)
            case ' ':
               pass
            case '\r':
                pass
            case '\t':
                pass
            case '\n':
                line += 1  
            case '"':    
                self.string()
            case _: 
                Lox.error(line, "Unexepected character.")
                
            
    def string(self):
        while self.peek() != '"' and not self.end():
            if self.peek() == '\n':
                line += 1
            self.advance()
        if self.end():
            Lox.error(line, "Unterminated String")
            return
        
        self.advance()  # consumes the terminating "
        
        value = self.source[self.start + 1: self.current - 1]
        self.addToken(STRING, value)
        
        
    def match(self, expected: str):
        if self.end():
            return False
        
        if self.source[self.current] != expected:
            return False
        
        self.current += 1
        return True
    
    def peek(self):
        if self.end():
            return '\0'
        return self.source[self.current]
    
    def end(self):
        return self.current >= len(self.source)
    
    def advance(self):
        self.current += 1
        return self.source[self.current - 1]
    
    def addToken(self, typeToken: TokenType, literal=None):
        text = self.source[self.start:self.current]
        token = Token(typeToken, text, literal, self.line)
        self.tokens.append(token)