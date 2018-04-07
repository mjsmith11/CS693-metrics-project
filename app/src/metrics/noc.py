import ast
from .astUtils import ClassNodeLister,FunctionNodeLister,InheritanceTreeBuilder
from ..lib.graph import Graph

class NOC:
    def __init__(self, filepath):
        self.file = filepath
        f = open(self.file)
        self.tree = ast.parse(f.read())
        f.close()

    def calculateAll(self):
        results = {}
        self.buildTree()
        for className in self.inheritanceTree.graph:
            if not (className=="~" or className=="object"):
                results[className] = self.calculateOne(className)
        return results

    def buildTree(self):
        treeBuilder = InheritanceTreeBuilder(False)
        treeBuilder.visit(self.tree)
        self.inheritanceTree = treeBuilder.getTree()

    def calculateOne(self, className):
        return len(self.inheritanceTree.graph[className])

