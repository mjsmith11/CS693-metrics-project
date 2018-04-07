import ast
from .astUtils import InheritanceTreeBuilder, ClassNodeLister
from ..lib.graph import Graph

class DIT:
    def __init__(self, filepath):
        self.file = filepath
        f = open(self.file)
        self.tree = ast.parse(f.read())
        f.close()
        self.classNames = []

    def findClasses(self):
        classVisiter = ClassNodeLister()
        classVisiter.visit(self.tree)

        classNodes = classVisiter.getClassNodes()
        for node in classNodes:
            self.classNames.append(node.name)

    def calculateAll(self, countObject = False):
        results = {}
        self.findClasses()
        self.buildTree()
        for className in self.inheritanceTree.graph:
            if className in self.classNames:
                results[className] = self.calculateOne(className, countObject)
        return results

    def buildTree(self):
        treeBuilder = InheritanceTreeBuilder(True)
        treeBuilder.visit(self.tree)
        self.inheritanceTree = treeBuilder.getTree()

    def calculateOne(self, className, countObject = False):
        currentNode = className
        depth = 0
        while len(self.inheritanceTree.graph[currentNode])>0:
            parent = self.inheritanceTree.graph[currentNode][0]
            if parent == "object":
                if countObject:
                    depth += 1
            elif not parent == "~":
                depth += 1
            currentNode = parent

        return depth




    