import ast
from .astUtils import ClassNodeLister, FunctionNodeLister

class WMC:
    def __init__(self, filepath):
        self.file = filepath
        f = open(self.file)
        self.tree = ast.parse(f.read())
        f.close()

    def calculateAll(self, countInit = False):
        results = {}
        classLister = ClassNodeLister()
        classLister.visit(self.tree)
        classes = classLister.getClassNodes()
        for classNode in classes:
            results[classNode.name] = self.calculateOne(classNode, countInit)
        return results

    def calculateOne(self, classNode, countInit = False):
        methodCount = 0
        functionLister = FunctionNodeLister()
        functionLister.visit(classNode)
        functions = functionLister.getFunctionNodes()

        for func in functions:
            if func.name == "__init__":
                if countInit:
                    methodCount += 1
            else:
                methodCount += 1
        return methodCount




    