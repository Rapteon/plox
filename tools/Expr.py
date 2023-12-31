import Lox
from Token import Token

class Expr:
   def accept(self, visitor):
       pass
class ExprVisitor:
   def visitBinary(self, expr):
       pass

   def visitGrouping(self, expr):
       pass

   def visitLiteral(self, expr):
       pass

   def visitUnary(self, expr):
       pass




class Binary(Expr):
   def __init__(self, left: Expr, operator: Token, right: Expr):
       self.left = left
       self.operator = operator
       self.right = right

   def accept(self, visitor: ExprVisitor):
       visitor.visitBinary()



class Grouping(Expr):
   def __init__(self, expression: Expr):
       self.expression = expression

   def accept(self, visitor: ExprVisitor):
       visitor.visitGrouping()



class Literal(Expr):
   def __init__(self, value):
       self.value = value

   def accept(self, visitor: ExprVisitor):
       visitor.visitLiteral()



class Unary(Expr):
   def __init__(self, operator: Token, right: Expr):
       self.operator = operator
       self.right = right

   def accept(self, visitor: ExprVisitor):
       visitor.visitUnary()



