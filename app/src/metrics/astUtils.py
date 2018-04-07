import ast
from ..lib.graph import Graph

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

# Creates a directed graph representing the inheritance structure of an ast node
# No base class listed is indicated by ~ as the parent class
class InheritanceTreeBuilder(ast.NodeVisitor):
    # upOrDown is a boolean indicating the direction of the tree's directed edges
    # If true, the edges will go from child class to parent class
    # If false, the edges will go from parent class to child class
    def __init__(self, upOrDown):
        self.upOrDown = upOrDown
        self.tree = Graph(True)

    def getTree(self):
        return self.tree

    def add_edge(self, parent, child):
        if self.upOrDown:
            self.tree.add_edge(child, parent)
        else:
            self.tree.add_edge(parent, child)

    def visit_ClassDef(self,node):
        if len(node.bases)>0:
            for base in node.bases:
                self.add_edge(base.id, node.name)
        else:
            self.add_edge("~", node.name)
        self.generic_visit(node)