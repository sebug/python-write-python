import ast
import astpretty
import astor
import sys

class Visitor(ast.NodeVisitor):
    def visit_connect_Call(self, node):
        keyword_names = [kw.arg for kw in node.keywords]
        if 'username' in keyword_names and 'password' in keyword_names:
            print('Ah ah ah!')
        elif len(node.args) >= 2:
            print('Ah ah ah positional!')
        self.generic_visit(node)
    
    def visit_Call(self, node):
        if node.func.id == 'connect':
            self.visit_connect_Call(node)
        else:
            self.generic_visit(node)


if len(sys.argv) < 2:
    print("Usage: main.py file_to_analyze.py")
    sys.exit(1)

def analyze_file_content(file_content):
    tree = ast.parse(file_content)
    visitor = Visitor()
    visitor.visit(tree)
    return tree

def analyze_file(f):
    with open(f, 'r') as file:
        file_content = file.read()
        analyzed = analyze_file_content(file_content)
        pretty_printed = astor.to_source(analyzed)
        print(pretty_printed)

    
analyze_file(sys.argv[1])
