import ast
from .astUtils import ClassNodeLister,FunctionNodeLister

class CBO:
    def __init__(self, filepath):
        self.file = filepath
        f = open(self.file)
        self.tree = ast.parse(f.read())
        f.close()
        self.classNodes = []

    def findClasses(self):
        classVisiter = ClassNodeLister()
        classVisiter.visit(self.tree)
        self.classNodes = classVisiter.getClassNodes()

    def playground(self):
        self.findClasses()
        couplingClass = self.classNodes[2]
        AttributeLister().visit(couplingClass)

class AttributeLister(ast.NodeVisitor):
    def __init__(self):
        self.attributesReferenced = []

    def getAttributeList(self):
        return self.attributesReferenced

    def visit_Attribute(self, node):
        self.attributesReferenced.append(node.attr)
        print(ast.dump(node))
        self.generic_visit(node)