import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: generate_ast <output directory>", file=sys.stderr)
        exit(64)
    outputDir = sys.argv[1]
    types = {
        "Binary": "left, operator, right",
        "Grouping": "expression",
        "Literal": "value",
        "Unary": "operator, right"
    }
    defineAst(outputDir, "Expr", types)
 
def defineAst(outputDir: str, baseName: str, types: dict[str]):
    path = outputDir + "/" + baseName + ".py"
    
    with open(path, "w") as f:
        f.write("import Lox\n\n")
        f.write("class " + baseName + ":\n")
    
    defineVisitor(baseName, types, path)
    
    for name in types:
        className = name
        fields = types[name]
        defineType(baseName, className, fields, path)

def defineType(baseName: str, className: str, fieldList: str, path: str):
    fields = fieldList.split(',')
    with open(path, "a") as f:
        f.write("class " + className + "("+baseName+"):\n")
        f.write("   def __init__(self, "+fieldList+"):\n")
        for field in fields:
            field = field.strip()
            f.write("       self."+field+" = "+field+"\n")
            
def defineVisitor(baseName: str, types, path: str):
    with open(path, "a") as f:
        f.write()        
        
        
if __name__ == "__main__":
    main()