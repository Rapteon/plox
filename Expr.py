import Lox
from Token import Token

class Expr:
   pass
class ExprVisitor:
   def visitBinary(self):
       pass

   def visitGrouping(self):
       pass

   def visitLiteral(self):
       pass

   def visitUnary(self):
       pass

class Binary(Expr):
   def __init__(self, left: Expr, operator: Token, right: Expr):
       self.left = left
       self.operator = operator
       self.right = right

   def accept(self, visitor: ExprVisitor):
       visitor.visitBinary(self)

class Grouping(Expr):
   def __init__(self, expression: Expr):
       self.expression = expression

   def accept(self, visitor: ExprVisitor):
       visitor.visitGrouping(self)

class Literal(Expr):
   def __init__(self, value):
       self.value = value

   def accept(self, visitor: ExprVisitor):
       visitor.visitLiteral(self)

class Unary(Expr):
   def __init__(self, operator: Token, right: Expr):
       self.operator = operator
       self.right = right

   def accept(self, visitor: ExprVisitor):
       visitor.visitUnary(self)

