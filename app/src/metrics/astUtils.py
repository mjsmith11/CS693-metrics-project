import ast

class ClassNodeLister(ast.NodeVisitor):
    def __init__(self):
        self.classNodes = []

    def getClassNodes(self):
        return self.classNodes

    def visit_ClassDef(self, node):
        self.classNodes.append(node)
        self.generic_visit(node)

class FunctionNodeLister(ast.NodeVisitor):
    def __init__(self):
        self.functionNodes = []

    def getFunctionNodes(self):
        return self.functionNodes

    def visit_FunctionDef(self, node):
        self.functionNodes.append(node)
        self.generic_visit(node)