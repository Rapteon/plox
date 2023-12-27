from Token import Token
from TokenType import TokenType
from Lox import error 

class Scanner:
    
    start = 0
    current = 0
    line = 1
    keywords = {
                "and": TokenType.AND,
                "class": TokenType.CLASS,
                "else": TokenType.ELSE,
                "false": TokenType.FALSE,
                "for": TokenType.FOR,
                "fun": TokenType.FUN,
                "if": TokenType.IF,
                "nil": TokenType.NIL,
                "or": TokenType.OR,
                "print": TokenType.PRINT,
                "return": TokenType.RETURN,
                "super": TokenType.SUPER,
                "this": TokenType.THIS,
                "true": TokenType.TRUE,
                "var": TokenType.VAR,
                "while": TokenType.WHILE
                }
    
    def __init__(self, source: str):
        self.source = source
        # self.source = "() {} != "
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
                self.addToken(TokenType.BANG_EQUAL) if self.match("=") else self.addToken(TokenType.BANG)   # example of ternary operator
            case '=':
                self.addToken(TokenType.EQUAL_EQUAL) if self.match("=") else self.addToken(TokenType.EQUAL)
            case '>':
                self.addToken(TokenType.GREATER_EQUAL) if self.match("=") else self.addToken(TokenType.GREATER)
            case '<':
                self.addToken(TokenType.LESS_EQUAL) if self.match("=") else self.addToken(TokenType.LESS)
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
                if self.isDigit(c):
                    self.number()
                elif self.isAlpha(c):
                    self.identifier()
                else:
                    error(self.line, "Unexepected character.")
                    
    
    def identifier(self):

        while self.isAlphaNumeric(self.peek()):
            self.advance()
            
        text = self.source[self.start : self.current]
        try:
            typeToken = self.keywords[text]
        except:
            typeToken = TokenType.IDENTIFIER
            
        self.addToken(typeToken)
    
    def isAlpha(self, c: chr) -> bool:
       if c == '_':
           return True
       return c.isalpha() 

    def isAlphaNumeric(self, c: chr) -> bool:
        return self.isAlpha(c) or self.isDigit(c)            
             
    def isDigit(self, num: int) -> bool:
        return num >= '0' and num <= '9'
    
    def number(self):
        while self.isDigit(self.peek()):
            self.advance()
        
        # find decimal point
        if self.peek() == '.' and self.isDigit(self.peekNext()):
            self.advance()
        while self.isDigit(self.peek()):
            self.advance()
        
        self.addToken(TokenType.NUMBER, float(self.source[self.start : self.current]))
    
    def peekNext(self) -> chr: # peeks 2 characters ahead
        if self.current+1 >= len(self.source):
            return '\0'
        return self.source[current+1]
                      
    def string(self):
        while self.peek() != '"' and not self.end():
            if self.peek() == '\n':
                line += 1
            self.advance()
        if self.end():
            error(self.line, "Unterminated String")
            return
        
        self.advance()  # consumes the terminating "
        
        value = self.source[self.start + 1: self.current - 1]
        self.addToken(TokenType.STRING, value)
             
    def match(self, expected: str) -> bool:
        if self.end():
            return False
        
        if self.source[self.current] != expected:
            return False
        
        self.current += 1
        return True
    
    def peek(self) -> chr:
        if self.end():
            return '\0'
        return self.source[self.current]
    
    def end(self) -> bool:
        return self.current >= len(self.source)
    
    def advance(self) -> chr:
        self.current += 1
        return self.source[self.current - 1]
    
    def addToken(self, typeToken: TokenType, literal=None):   # in the book, the author made the literal parameter be any object and that is because they can be strings or floats, so we cant just have one type
        text = self.source[self.start : self.current]
        token = Token(typeToken, text, literal, self.line)
        self.tokens.append(token)