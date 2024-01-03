from Expr import Expr, ExprVisitor, Binary, Grouping, Literal, Unary
from Token import Token
from TokenType import TokenType


class AstPrinter(ExprVisitor):
    def print(self, expr: Expr) -> str:
        return expr.accept(
            self
        )  # really need to understand visitor design pattern in python

    def visitBinaryExpr(self, expr: Binary):
        return self.parenthesize(expr.operator.lexeme, expr.left, expr.right)

    def visitGroupingExpr(self, expr: Grouping):
        return self.parenthesize("group", expr.expression)

    def visitLiteralExpr(self, expr: Literal) -> str:
        if expr.value is None:
            return "nil"
        return str(expr.value)

    def visitUnaryExpr(self, expr: Unary):
        return self.parenthesize(expr.operator.lexeme, expr.right)

    def parenthesize(self, name, *exprs):
        builder = ""
        builder += "(" + name
        for expr in exprs:
            builder += " "
            builder += str(expr.accept(self))
        builder += ")"

        return str(builder)


def main():
    exp = Binary(
        Unary(Token(TokenType.MINUS, "-", "", 1), Literal(123)),
        Token(TokenType.STAR, "*", "", 1),
        Grouping(Literal(45.67)),
    )
    printer = AstPrinter()
    print(printer.print(exp))


if __name__ == "__main__":
    main()

# SO MUCH DEBUGGING JUST BECAUSE I WASNT RETURNING ANYTHING FROM EXPR BRUH
