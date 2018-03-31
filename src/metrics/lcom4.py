import ast
import astUtils
import sys
sys.path.append('../lib')
import graph

class LCOM4:
    def __init__(self, filepath):
        self.file = filepath
        self.tree = ast.parse(open(self.file).read())
        self.classNodes = []

    def calculateModuleLOCM4(self):
        results = {}
        self.findClasses()
        for classNode in self.classNodes:
            results[classNode.name] = self.calculateClassLOCM4(classNode)
        return results

    def findClasses(self):
        classVisiter = astUtils.ClassNodeLister()
        classVisiter.visit(self.tree)
        self.classNodes = classVisiter.getClassNodes()

    def calculateClassLOCM4(self, classNode):
        functionLister = astUtils.FunctionNodeLister()
        functionLister.visit(classNode)
        functions = functionLister.getFunctionNodes()
        connectionGraph = graph.Graph(False)
        for function in functions:
            if function.name == "__init__":
                continue
            attributeLister = AttributeLister()
            attributeLister.visit(function)
            attributes = attributeLister.getAttributeList()
            for attribute in attributes:
                connectionGraph.add_edge(function.name,attribute)
        return connectionGraph.countConnectedComponents()

class AttributeLister(ast.NodeVisitor):
    def __init__(self):
        self.attributesReferenced = []

    def getAttributeList(self):
        return self.attributesReferenced

    def visit_Attribute(self, node):
        if getattr(node.value, 'id', "") == "self" or getattr(node.value, 'attr', "") == "self": #ensure that we don't count attributes of other classes
            self.attributesReferenced.append(node.attr)
        self.generic_visit(node)