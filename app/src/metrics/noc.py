import ast
from .astUtils import InheritanceTreeBuilder,ClassNodeLister

class NOC:
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

    def calculateAll(self):
        results = {}
        self.findClasses()
        self.buildTree()
        for className in self.inheritanceTree.graph:
            if className in self.classNames:
                results[className] = self.calculateOne(className)
        return results

    def buildTree(self):
        treeBuilder = InheritanceTreeBuilder(False)
        treeBuilder.visit(self.tree)
        self.inheritanceTree = treeBuilder.getTree()

    def calculateOne(self, className):
        return len(self.inheritanceTree.graph[className])

