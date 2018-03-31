import unittest
import ast
import os.path
from ...src.metrics import astUtils
from ...src.metrics.lcom4 import AttributeLister
from ...src.metrics.lcom4 import LCOM4

class TestLCOM4(unittest.TestCase):
    def getPath(self):
        my_path = os.path.abspath(os.path.dirname(__file__))
        return os.path.join(my_path,"../files/sample1.py")

    def test_Calculation(self):
        obj = LCOM4(self.getPath())
        result = obj.calculateModuleLCOM4()
        self.assertEqual(len(result),11,"number of classes analyzed")
        self.assertEqual(result["CohesionExample1"],2,"LCOM4 for CohesionExample1")
        self.assertEqual(result["CohesionExample2"],1,"LCOM4 for CohesionExample2")
        self.assertEqual(result["CouplingExample1"],1,"LCOM4 for CouplingExample1")
        self.assertEqual(result["CouplingExample2"],0,"LCOM4 for CouplingExample2")
        self.assertEqual(result["DepthOfInheritanceExample1"],0,"LCOM4 for DepthOfInheritanceExample1")
        self.assertEqual(result["DepthOfInheritanceExample2"],0,"LCOM4 for DepthOfInheritanceExample2")
        self.assertEqual(result["DepthOfInheritanceExample3"],0,"LCOM4 for DepthOfInheritanceExample3")
        self.assertEqual(result["DepthOfInheritanceExample4"],0,"LCOM4 for DepthOfInheritanceExample4")
        self.assertEqual(result["NumberOfChildrenExample1"],0,"LCOM4 for NumberOfChildrenExample1")
        self.assertEqual(result["NumberOfChildrenExample2"],0,"LCOM4 for NumberOfChildrenExample2")
        self.assertEqual(result["NumberOfChildrenExample3"],0,"LCOM4 for NumberOfChildrenExample3")

class TestAttributeLister(unittest.TestCase):
    def getPath(self):
        my_path = os.path.abspath(os.path.dirname(__file__))
        return os.path.join(my_path,"../files/sample1.py")

    def test_noExternalAttributes(self):
        f = open(self.getPath())
        tree = ast.parse(f.read())
        f.close()
        classVisiter = astUtils.ClassNodeLister()
        classVisiter.visit(tree)
        classNodes = classVisiter.getClassNodes()

        myClass = classNodes[0]
        self.assertEqual(myClass.name, "CohesionExample1", "Checking that we found the right class")

        functionLister = astUtils.FunctionNodeLister()
        functionLister.visit(myClass)
        functions = functionLister.getFunctionNodes()

        myFunction = functions[4]
        self.assertEqual(myFunction.name, "d", "Checking that we found the right function")

        attributeLister = AttributeLister()
        attributeLister.visit(myFunction)
        attributes = attributeLister.getAttributeList()

        self.assertEqual(len(attributes),2,"Length of attribute list")
        self.assertTrue("y" in attributes, "Variable attribute y")
        self.assertTrue("e" in attributes, "Variable attribute e")

    def test_ExternalAttributes(self):
        f = open(self.getPath())
        tree = ast.parse(f.read())
        f.close()
        classVisiter = astUtils.ClassNodeLister()
        classVisiter.visit(tree)
        classNodes = classVisiter.getClassNodes()

        myClass = classNodes[2]
        self.assertEqual(myClass.name, "CouplingExample1", "Checking that we found the right class")

        functionLister = astUtils.FunctionNodeLister()
        functionLister.visit(myClass)
        functions = functionLister.getFunctionNodes()

        myFunction = functions[1]
        self.assertEqual(myFunction.name, "n1", "Checking that we found the right function")

        attributeLister = AttributeLister()
        attributeLister.visit(myFunction)
        attributes = attributeLister.getAttributeList()

        self.assertEqual(len(attributes),2,"Length of attribute list")
        self.assertEqual(attributes[0],"otherClass", "First Attribute")
        self.assertEqual(attributes[1],"otherClass", "Second Attribute")