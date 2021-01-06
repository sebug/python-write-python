import ast
import astpretty
import sys

if len(sys.argv) < 2:
    print("Usage: main.py file_to_analyze.py")
    sys.exit(1)

def analyze_file_content(file_content):
    tree = ast.parse(file_content)
    return tree

def analyze_file(f):
    with open(f, 'r') as file:
        file_content = file.read()
        analyzed = analyze_file_content(file_content)
        print(analyzed)


analyze_file(sys.argv[1])
