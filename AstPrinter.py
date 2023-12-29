# from Expr import Expr, ExprVisitor, Binary, Grouping, Literal, Unary


# class AstPrinter(ExprVisitor):
#     def print(self, expr: Expr) -> str:
#         return expr.accept(self)

#     def visitBinary(self, expr: Binary):
#         return parenthesize(expr.operator.lexeme
#                             expr.left, expr.right)
        
#     def parenthesize(self, name, *exprs):
#         pass
    
# need to understand visitor pattern better