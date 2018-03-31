"""
Class for calculation Lack of Cohesion Metric 4. Construct with the file path
Then call calculateModuleLCOM4 to obtain a dictionary of LCOM4 Values
"""
import ast
from .astUtils import ClassNodeLister,FunctionNodeLister
from ..lib import graph

class LCOM4:
    def __init__(self, filepath):
        self.file = filepath
        f = open(self.file)
        self.tree = ast.parse(f.read())
        f.close()
        self.classNodes = []

    """ Returns a dictionary keyed by class name and value LCOM4"""
    def calculateModuleLCOM4(self):
        results = {}
        self.findClasses()
        for classNode in self.classNodes:
            results[classNode.name] = self.calculateClassLCOM4(classNode)
        return results

    def findClasses(self):
        classVisiter = ClassNodeLister()
        classVisiter.visit(self.tree)
        self.classNodes = classVisiter.getClassNodes()

    def calculateClassLCOM4(self, classNode):
        functionLister = FunctionNodeLister()
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