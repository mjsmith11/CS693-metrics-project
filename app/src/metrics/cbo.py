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
        for cl in self.classNodes:
            print(cl.name)
            var = ListVariablesOfType("CouplingExample1",False)
            var.visit(cl)
            print(var.getVariablesList())
            #var = ClassVariableLister()
            #var.visit(cl)
            #print(var.getVariablesList()

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