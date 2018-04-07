import unittest
import ast
import os.path
from ...src.metrics import astUtils

class TestAstUtils(unittest.TestCase):
    def getPath(self):
        my_path = os.path.abspath(os.path.dirname(__file__))
        return os.path.join(my_path,"../files/sample1.py")

    def test_ClassNodeLister(self):
        f = open(self.getPath())
        tree = ast.parse(f.read())
        f.close()
        classVisiter = astUtils.ClassNodeLister()
        classVisiter.visit(tree)
        classNodes = classVisiter.getClassNodes()
        self.assertEqual(len(classNodes), 11, "Number of Classes found")
        self.assertTrue(self.nameExistsInList(classNodes,"CohesionExample1"),"Looking for CohesionExample1")
        self.assertTrue(self.nameExistsInList(classNodes,"CohesionExample2"),"Looking for CohesionExample2")
        self.assertTrue(self.nameExistsInList(classNodes,"CouplingExample1"),"Looking for CouplingExample1")
        self.assertTrue(self.nameExistsInList(classNodes,"CouplingExample2"),"Looking for CouplingExample2")
        self.assertTrue(self.nameExistsInList(classNodes,"DepthOfInheritanceExample1"),"Looking for DepthOfInheritanceExample1")
        self.assertTrue(self.nameExistsInList(classNodes,"DepthOfInheritanceExample2"),"Looking for DepthOfInheritanceExample2")
        self.assertTrue(self.nameExistsInList(classNodes,"DepthOfInheritanceExample3"),"Looking for DepthOfInheritanceExample3")
        self.assertTrue(self.nameExistsInList(classNodes,"DepthOfInheritanceExample4"),"Looking for DepthOfInheritanceExample4")
        self.assertTrue(self.nameExistsInList(classNodes,"NumberOfChildrenExample1"),"Looking for NumberOfChildrenExample1")
        self.assertTrue(self.nameExistsInList(classNodes,"NumberOfChildrenExample2"),"Looking for NumberOfChildrenExample2")
        self.assertTrue(self.nameExistsInList(classNodes,"NumberOfChildrenExample3"),"Looking for NumberOfChildrenExample3")

    def test_FunctionNodeLister(self):
        f = open(self.getPath())
        tree = ast.parse(f.read())
        f.close()
        classVisiter = astUtils.ClassNodeLister()
        classVisiter.visit(tree)
        classNodes = classVisiter.getClassNodes()

        myClass = classNodes[0]
        self.assertEqual(myClass.name,"CohesionExample1", "Make sure we have the right class")

        functionVisiter = astUtils.FunctionNodeLister()
        functionVisiter.visit(myClass)
        functionNodes = functionVisiter.getFunctionNodes()
        
        self.assertEqual(len(functionNodes),6,"Number of functions found")
        self.assertTrue(self.nameExistsInList(functionNodes,"__init__"), "Looking for __init__")
        self.assertTrue(self.nameExistsInList(functionNodes,"a"), "Looking for a")
        self.assertTrue(self.nameExistsInList(functionNodes,"b"), "Looking for b")
        self.assertTrue(self.nameExistsInList(functionNodes,"c"), "Looking for c")
        self.assertTrue(self.nameExistsInList(functionNodes,"d"), "Looking for d")
        self.assertTrue(self.nameExistsInList(functionNodes,"e"), "Looking for e")

    def test_InheritanceTreeBuilderUp(self):
            f = open(self.getPath())
            tree = ast.parse(f.read())
            f.close()
            treeBuilder = astUtils.InheritanceTreeBuilder(True)
            treeBuilder.visit(tree)
            graph = treeBuilder.getTree()
            self.assertTrue("~" in graph.graph["CohesionExample1"], "CohesionExample1 node")
            self.assertTrue("~" in graph.graph["CohesionExample2"], "CohesionExample2 node")
            self.assertTrue("~" in graph.graph["CouplingExample1"], "CouplingExample1 node")
            self.assertTrue("~" in graph.graph["CouplingExample2"], "CouplingExample2 node")
            self.assertTrue("object" in graph.graph["DepthOfInheritanceExample1"], "DepthOfInheritanceExample1 node")
            self.assertTrue("DepthOfInheritanceExample1" in graph.graph["DepthOfInheritanceExample2"], "DepthOfInheritanceExample2 node")
            self.assertTrue("~" in graph.graph["DepthOfInheritanceExample3"], "DepthOfInheritanceExample3 node")
            self.assertTrue("DepthOfInheritanceExample3" in graph.graph["DepthOfInheritanceExample4"], "DepthOfInheritanceExample4 node")
            self.assertTrue("~" in graph.graph["NumberOfChildrenExample1"], "NumberOfChildrenExample1 node")
            self.assertTrue("NumberOfChildrenExample1" in graph.graph["NumberOfChildrenExample2"], "NumberOfChildrenExample2 node")
            self.assertTrue("NumberOfChildrenExample1" in graph.graph["NumberOfChildrenExample3"], "NumberOfChildrenExample3 node")

    def test_InheritanceTreeBuilderDown(self):
        f = open(self.getPath())
        tree = ast.parse(f.read())
        f.close()
        treeBuilder = astUtils.InheritanceTreeBuilder(False)
        treeBuilder.visit(tree)
        graph = treeBuilder.getTree()
        self.assertTrue("DepthOfInheritanceExample1" in graph.graph["object"], "DepthOfInheritanceExample1 under object")
        self.assertEqual(len(graph.graph["CohesionExample1"]), 0, "Nothing Under CohesionExample1")
        self.assertEqual(len(graph.graph["CohesionExample2"]), 0, "Nothing Under CohesionExample2")
        self.assertEqual(len(graph.graph["CouplingExample1"]), 0, "Nothing Under CouplingExample1")
        self.assertEqual(len(graph.graph["CouplingExample2"]), 0, "Nothing Under CouplingExample2")
        self.assertTrue("DepthOfInheritanceExample2" in graph.graph["DepthOfInheritanceExample1"], "DepthOfInheritanceExample2 under DepthOfInheritanceExample1")
        self.assertEqual(len(graph.graph["DepthOfInheritanceExample2"]), 0, "Nothing Under DepthOfInheritanceExample2")
        self.assertTrue("DepthOfInheritanceExample4" in graph.graph["DepthOfInheritanceExample3"], "DepthOfInheritanceExample4 under DepthOfInheritanceExample3")
        self.assertEqual(len(graph.graph["DepthOfInheritanceExample4"]), 0, "Nothing Under DepthOfInheritanceExample4")
        self.assertTrue("NumberOfChildrenExample2" in graph.graph["NumberOfChildrenExample1"], "NumberOfChildrenExample2 under NumberOfChildrenExample1")
        self.assertTrue("NumberOfChildrenExample3" in graph.graph["NumberOfChildrenExample1"], "NumberOfChildrenExample3 under NumberOfChildrenExample1")
        self.assertEqual(len(graph.graph["NumberOfChildrenExample2"]), 0, "Nothing Under NumberOfChildrenExample2")
        self.assertEqual(len(graph.graph["NumberOfChildrenExample3"]), 0, "Nothing Under NumberOfChildrenExample3")
            


    """Returns true if it finds an element in the list with a name 
    attribute matching the passed name. Returns false otherwise."""
    def nameExistsInList(self, list, name):
        for e in list:
            if getattr(e,'name',"") == name:
                return True
        return False
