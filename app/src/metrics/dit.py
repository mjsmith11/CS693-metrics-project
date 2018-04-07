import ast
from .astUtils import InheritanceTreeBuilder
from ..lib.graph import Graph

class DIT:
    def __init__(self, filepath):
        self.file = filepath
        f = open(self.file)
        self.tree = ast.parse(f.read())
        f.close()

    def calculateAll(self, countObject = False):
        results = {}
        self.buildTree()
        for className in self.inheritanceTree.graph:
            if not (className=="~" or className=="object"):
                results[className] = self.calculateOne(className, countObject)
        return results

    def buildTree(self):
        treeBuilder = InheritanceTreeBuilder(True)
        treeBuilder.visit(self.tree)
        self.inheritanceTree = treeBuilder.getTree()

    def calculateOne(self, className, countObject = False):
        currentNode = className
        depth = 0
        while not(currentNode == "object" or currentNode == "~"):
            parent = self.inheritanceTree.graph[currentNode][0]
            if parent == "object":
                if countObject:
                    depth += 1
            elif not parent == "~":
                depth += 1
            currentNode = parent

        return depth




    