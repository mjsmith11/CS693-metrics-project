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

    def calculateAllCBO(self):
        results = {}
        self.findClasses()
        for i in range(0, len(self.classNodes)):
            for j in range (i+1, len(self.classNodes)):
                classA = self.classNodes[i]
                classB = self.classNodes[j]
                key = classA.name + " <-> "+classB.name
                results[key] = self.calculateOneCBO(classA, classB)
        return results


    def calculateOneCBO(self, classNodeA, classNodeB):
        AtoBUsages = self.findUsages(classNodeA, classNodeB)
        BtoAUsages = self.findUsages(classNodeB, classNodeA)
        return len(AtoBUsages) + len(BtoAUsages)

    #Returns a list of methods and variables of class A used in class B
    def findUsages(self, classNodeA, classNodeB):
        usages = []
        classVarLister = ListVariablesOfType(classNodeA.name, True)
        classVarLister.visit(classNodeB)
        typeClassAVars = classVarLister.getVariablesList()
        funcLister = FunctionNodeLister()
        funcLister.visit(classNodeB)
        classBFuncs = funcLister.getFunctionNodes()
        for func in classBFuncs:
            localVarLister = ListVariablesOfType(classNodeA.name, False)
            localVarLister.visit(func)
            typeClassALocalVars = localVarLister.getVariablesList()
            usageFinder = ListUsageOfSpecifiedVars(typeClassAVars, typeClassALocalVars)
            usageFinder.visit(func)
            thisFuncUsage = usageFinder.getUsageList()
            for u in thisFuncUsage:
                if u not in usages:
                    usages.append(u)
        return usages


#Lists methods and variables of the specified variables that are used.
class ListUsageOfSpecifiedVars(ast.NodeVisitor):
    def __init__(self, classVars, localVars):
        self.classVars = classVars
        self.localVars = localVars
        self.usages = []

    def getUsageList(self):
        return self.usages

    def visit_Attribute(self, node):
        value = node.value
        if isinstance(value, ast.Attribute):
            # Check to see if it's a call on a specified class var.
            if value.attr in self.classVars and value.value.id == "self":
                self.usages.append(node.attr)
        if isinstance(value, ast.Name):
            # Check to see if it's a call on a specified local var
            if value.id in self.localVars:
                self.usages.append(node.attr)
        self.generic_visit(node)


# List all variables of `searchType` as determined by constructor calls in the node searched.
# If `attributeVars` is True, a list of class attributes will be built.
# If `attributeVars` is False, a list of local variables will be built.
class ListVariablesOfType(ast.NodeVisitor):
    def __init__(self, searchType, attributeVars):
        self.variables = []
        self.type = searchType
        self.attributeVars = attributeVars

    def getVariablesList(self):
        return self.variables

    def visit_Assign(self, node):
        value = getattr(node, 'value', None)
        if isinstance(value, ast.Call): # Is it making a call on the RHS
            func = getattr(value, 'func', None)
            if isinstance(func,ast.Name) and func.id==self.type: # Does RHS fun have the name we are looking for?
                for target in node.targets:
                    if self.attributeVars:
                        if isinstance(target,ast.Attribute) and target.value.id == "self": #is the LHS an attribute belonging to self?
                            if target.attr not in self.variables:
                                self.variables.append(target.attr)
                    else:
                        if isinstance(target,ast.Name): # is the target a name?
                            if target.id not in self.variables:
                                self.variables.append(target.id)
        self.generic_visit(node)