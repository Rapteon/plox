import sys


hadError = False

def main():
    if len(sys.argv) > 2:
        print("Usage: plox [script]")
        exit(64)
    elif len(sys.argv) == 2:
        runFile(sys.argv[1])
    else:
        runPrompt()

def runFile(path):
    contents = ""
    with open(path, "r") as f:
        contents += f.read() 
    run(contents)
    if (hadError):
        exit(65)

def runPrompt():
    while(True):
        print("> ", end="")
        line = input()
        if (line == None):
            break
        run(line)
        hadError = False
        
def run(source):

    tokens = []

    
    for token in tokens:
        print(token)
        
def error(line, message):
    report(line, "", message)

def report(line, where, message):
    print("[line " + line + "] Error" + where + ": " + message, file=sys.stderr)
    hadError = True


main()