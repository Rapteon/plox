import sys


def main():
    if len(sys.argv) != 2:
        print("Usage: generate_ast <output directory>", file=sys.stderr)
        exit(64)
    outputDir = sys.argv[1]
    types = {
        "Binary": "left: Expr, operator: Token, right: Expr",
        "Grouping": "expression: Expr",
        "Literal": "value",
        "Unary": "operator: Token, right: Expr",
    }
    defineAst(outputDir, "Expr", types)


def defineAst(outputDir: str, baseName: str, types):
    path = outputDir + "/" + baseName + ".py"

    with open(path, "w") as f:
        f.write("import Lox\n")
        f.write("from Token import Token\n\n")
        f.write("class " + baseName + ":\n")
        f.write("   def accept(self, visitor):\n")
        f.write("       pass\n")

    defineVisitor(baseName, types, path)

    for name in types:
        className = name
        fields = types[name]
        defineType(baseName, className, fields, path)


def defineType(baseName: str, className: str, fieldList: str, path: str):
    fields = fieldList.split(",")

    with open(path, "a") as f:
        f.write("class " + className + "(" + baseName + "):\n")
        f.write("   def __init__(self, " + fieldList + "):\n")

        for field in fields:
            field = field.strip()
            colonIndex = field.find(":")
            if colonIndex != -1:
                field = field[0:colonIndex]
            f.write("       self." + field + " = " + field + "\n")

        f.write("\n")
        f.write("   def accept(self, visitor: ExprVisitor):\n")
        f.write("       visitor.visit" + className + "()\n\n\n\n")


def defineVisitor(baseName: str, types, path: str):
    with open(path, "a") as f:
        f.write("class ExprVisitor:\n")

        for tipo in types:
            f.write("   def visit" + tipo + "(self, expr):\n")
            f.write("       pass\n\n")
        f.write("\n\n\n")


if __name__ == "__main__":
    main()
