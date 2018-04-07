import unittest
import ast
import os.path
from ...src.metrics.cbo import CBO, ListUsageOfSpecifiedVars, ListVariablesOfType
from ...src.metrics import astUtils

class testCBO(unittest.TestCase):
    def getPath(self):
        my_path = os.path.abspath(os.path.dirname(__file__))
        return os.path.join(my_path,"../files/sample1.py")

    def test_Calculation(self):
        cbo = CBO(self.getPath())
        results = cbo.calculateAllCBO()
        self.assertEqual(len(results), 55, "Number of results")
        self.assertEqual(results["CohesionExample1 <-> CohesionExample2"],0,"CBO value CohesionExample1 <-> CohesionExample2")
        self.assertEqual(results["CohesionExample1 <-> CouplingExample1"],0,"CBO value CohesionExample1 <-> CouplingExample1")
        self.assertEqual(results["CohesionExample1 <-> CouplingExample2"],0,"CBO value CohesionExample1 <-> CouplingExample2")
        self.assertEqual(results["CohesionExample1 <-> DepthOfInheritanceExample1"],0,"CBO value CohesionExample1 <-> DepthOfInheritanceExample1")
        self.assertEqual(results["CohesionExample1 <-> DepthOfInheritanceExample2"],0,"CBO value CohesionExample1 <-> DepthOfInheritanceExample2")
        self.assertEqual(results["CohesionExample1 <-> DepthOfInheritanceExample3"],0,"CBO value CohesionExample1 <-> DepthOfInheritanceExample3")
        self.assertEqual(results["CohesionExample1 <-> DepthOfInheritanceExample4"],0,"CBO value CohesionExample1 <-> DepthOfInheritanceExample4")
        self.assertEqual(results["CohesionExample1 <-> NumberOfChildrenExample1"],0,"CBO value CohesionExample1 <-> NumberOfChildrenExample1")
        self.assertEqual(results["CohesionExample1 <-> NumberOfChildrenExample2"],0,"CBO value CohesionExample1 <-> NumberOfChildrenExample2")
        self.assertEqual(results["CohesionExample1 <-> NumberOfChildrenExample3"],0,"CBO value CohesionExample1 <-> NumberOfChildrenExample3")
        self.assertEqual(results["CohesionExample2 <-> CouplingExample1"],0,"CBO value CohesionExample2 <-> CouplingExample1")
        self.assertEqual(results["CohesionExample2 <-> CouplingExample2"],0,"CBO value CohesionExample2 <-> CouplingExample2")
        self.assertEqual(results["CohesionExample2 <-> DepthOfInheritanceExample1"],0,"CBO value CohesionExample2 <-> DepthOfInheritanceExample1")
        self.assertEqual(results["CohesionExample2 <-> DepthOfInheritanceExample2"],0,"CBO value CohesionExample2 <-> DepthOfInheritanceExample2")
        self.assertEqual(results["CohesionExample2 <-> DepthOfInheritanceExample3"],0,"CBO value CohesionExample2 <-> DepthOfInheritanceExample3")
        self.assertEqual(results["CohesionExample2 <-> DepthOfInheritanceExample4"],0,"CBO value CohesionExample2 <-> DepthOfInheritanceExample4")
        self.assertEqual(results["CohesionExample2 <-> NumberOfChildrenExample1"],0,"CBO value CohesionExample2 <-> NumberOfChildrenExample1")
        self.assertEqual(results["CohesionExample2 <-> NumberOfChildrenExample2"],0,"CBO value CohesionExample2 <-> NumberOfChildrenExample2")
        self.assertEqual(results["CohesionExample2 <-> NumberOfChildrenExample3"],0,"CBO value CohesionExample2 <-> NumberOfChildrenExample3")
        self.assertEqual(results["CouplingExample1 <-> CouplingExample2"],3,"CBO value CouplingExample1 <-> CouplingExample2")
        self.assertEqual(results["CouplingExample1 <-> DepthOfInheritanceExample1"],0,"CBO value CouplingExample1 <-> DepthOfInheritanceExample1")
        self.assertEqual(results["CouplingExample1 <-> DepthOfInheritanceExample2"],0,"CBO value CouplingExample1 <-> DepthOfInheritanceExample2")
        self.assertEqual(results["CouplingExample1 <-> DepthOfInheritanceExample3"],0,"CBO value CouplingExample1 <-> DepthOfInheritanceExample3")
        self.assertEqual(results["CouplingExample1 <-> DepthOfInheritanceExample4"],0,"CBO value CouplingExample1 <-> DepthOfInheritanceExample4")
        self.assertEqual(results["CouplingExample1 <-> NumberOfChildrenExample1"],0,"CBO value CouplingExample1 <-> NumberOfChildrenExample1")
        self.assertEqual(results["CouplingExample1 <-> NumberOfChildrenExample2"],0,"CBO value CouplingExample1 <-> NumberOfChildrenExample2")
        self.assertEqual(results["CouplingExample1 <-> NumberOfChildrenExample3"],0,"CBO value CouplingExample1 <-> NumberOfChildrenExample3")
        self.assertEqual(results["CouplingExample2 <-> DepthOfInheritanceExample1"],0,"CBO value CouplingExample2 <-> DepthOfInheritanceExample1")
        self.assertEqual(results["CouplingExample2 <-> DepthOfInheritanceExample2"],0,"CBO value CouplingExample2 <-> DepthOfInheritanceExample2")
        self.assertEqual(results["CouplingExample2 <-> DepthOfInheritanceExample3"],0,"CBO value CouplingExample2 <-> DepthOfInheritanceExample3")
        self.assertEqual(results["CouplingExample2 <-> DepthOfInheritanceExample4"],0,"CBO value CouplingExample2 <-> DepthOfInheritanceExample4")
        self.assertEqual(results["CouplingExample2 <-> NumberOfChildrenExample1"],0,"CBO value CouplingExample2 <-> NumberOfChildrenExample1")
        self.assertEqual(results["CouplingExample2 <-> NumberOfChildrenExample2"],0,"CBO value CouplingExample2 <-> NumberOfChildrenExample2")
        self.assertEqual(results["CouplingExample2 <-> NumberOfChildrenExample3"],0,"CBO value CouplingExample2 <-> NumberOfChildrenExample3")
        self.assertEqual(results["DepthOfInheritanceExample1 <-> DepthOfInheritanceExample2"],0,"CBO value DepthOfInheritanceExample1 <-> DepthOfInheritanceExample2")
        self.assertEqual(results["DepthOfInheritanceExample1 <-> DepthOfInheritanceExample3"],0,"CBO value DepthOfInheritanceExample1 <-> DepthOfInheritanceExample3")
        self.assertEqual(results["DepthOfInheritanceExample1 <-> DepthOfInheritanceExample4"],0,"CBO value DepthOfInheritanceExample1 <-> DepthOfInheritanceExample4")
        self.assertEqual(results["DepthOfInheritanceExample1 <-> NumberOfChildrenExample1"],0,"CBO value DepthOfInheritanceExample1 <-> NumberOfChildrenExample1")
        self.assertEqual(results["DepthOfInheritanceExample1 <-> NumberOfChildrenExample2"],0,"CBO value DepthOfInheritanceExample1 <-> NumberOfChildrenExample2")
        self.assertEqual(results["DepthOfInheritanceExample1 <-> NumberOfChildrenExample3"],0,"CBO value DepthOfInheritanceExample1 <-> NumberOfChildrenExample3")
        self.assertEqual(results["DepthOfInheritanceExample2 <-> DepthOfInheritanceExample3"],0,"CBO value DepthOfInheritanceExample2 <-> DepthOfInheritanceExample3")
        self.assertEqual(results["DepthOfInheritanceExample2 <-> DepthOfInheritanceExample4"],0,"CBO value DepthOfInheritanceExample2 <-> DepthOfInheritanceExample4")
        self.assertEqual(results["DepthOfInheritanceExample2 <-> NumberOfChildrenExample1"],0,"CBO value DepthOfInheritanceExample2 <-> NumberOfChildrenExample1")
        self.assertEqual(results["DepthOfInheritanceExample2 <-> NumberOfChildrenExample2"],0,"CBO value DepthOfInheritanceExample2 <-> NumberOfChildrenExample2")
        self.assertEqual(results["DepthOfInheritanceExample2 <-> NumberOfChildrenExample3"],0,"CBO value DepthOfInheritanceExample2 <-> NumberOfChildrenExample3")
        self.assertEqual(results["DepthOfInheritanceExample3 <-> DepthOfInheritanceExample4"],0,"CBO value DepthOfInheritanceExample3 <-> DepthOfInheritanceExample4")
        self.assertEqual(results["DepthOfInheritanceExample3 <-> NumberOfChildrenExample1"],0,"CBO value DepthOfInheritanceExample3 <-> NumberOfChildrenExample1")
        self.assertEqual(results["DepthOfInheritanceExample3 <-> NumberOfChildrenExample2"],0,"CBO value DepthOfInheritanceExample3 <-> NumberOfChildrenExample2")
        self.assertEqual(results["DepthOfInheritanceExample3 <-> NumberOfChildrenExample3"],0,"CBO value DepthOfInheritanceExample3 <-> NumberOfChildrenExample3")
        self.assertEqual(results["DepthOfInheritanceExample4 <-> NumberOfChildrenExample1"],0,"CBO value DepthOfInheritanceExample4 <-> NumberOfChildrenExample1")
        self.assertEqual(results["DepthOfInheritanceExample4 <-> NumberOfChildrenExample2"],0,"CBO value DepthOfInheritanceExample4 <-> NumberOfChildrenExample2")
        self.assertEqual(results["DepthOfInheritanceExample4 <-> NumberOfChildrenExample3"],0,"CBO value DepthOfInheritanceExample4 <-> NumberOfChildrenExample3")
        self.assertEqual(results["NumberOfChildrenExample1 <-> NumberOfChildrenExample2"],0,"CBO value NumberOfChildrenExample1 <-> NumberOfChildrenExample2")
        self.assertEqual(results["NumberOfChildrenExample1 <-> NumberOfChildrenExample3"],0,"CBO value NumberOfChildrenExample1 <-> NumberOfChildrenExample3")
        self.assertEqual(results["NumberOfChildrenExample2 <-> NumberOfChildrenExample3"],0,"CBO value NumberOfChildrenExample2 <-> NumberOfChildrenExample3")


class TestListUsageOfSpecifiedVars(unittest.TestCase):
    def getPath(self):
        my_path = os.path.abspath(os.path.dirname(__file__))
        return os.path.join(my_path,"../files/sample1.py")

    def test_FindingClassVarUsage(self):
        f = open(self.getPath())
        tree = ast.parse(f.read())
        f.close()
        classVisiter = astUtils.ClassNodeLister()
        classVisiter.visit(tree)
        classNodes = classVisiter.getClassNodes()

        myClass = classNodes[2]
        self.assertEqual(myClass.name, "CouplingExample1", "Checking that we found the right class")

        lister = ListUsageOfSpecifiedVars(["otherClass"],[])
        lister.visit(myClass)
        results = lister.getUsageList()

        self.assertEqual(len(results),2,"Expecting 2 elements in results")
        self.assertTrue("m1" in results, "Looking for m1")
        self.assertTrue("x" in results, "Looking for x")

    def test_FindingLocalVarUsage(self):
        f = open(self.getPath())
        tree = ast.parse(f.read())
        f.close()
        classVisiter = astUtils.ClassNodeLister()
        classVisiter.visit(tree)
        classNodes = classVisiter.getClassNodes()

        myClass = classNodes[3]
        self.assertEqual(myClass.name, "CouplingExample2", "Checking that we found the right class")

        lister = ListUsageOfSpecifiedVars([],["localOtherClass"])
        lister.visit(myClass)
        results = lister.getUsageList()

        self.assertEqual(len(results),1,"Expecting 1 elements in results")
        self.assertTrue("n1" in results, "Looking for n1")

class TestListVariablesOfType(unittest.TestCase):
    def getPath(self):
        my_path = os.path.abspath(os.path.dirname(__file__))
        return os.path.join(my_path,"../files/sample1.py")
    
    def test_FindingClassVars(self):
        f = open(self.getPath())
        tree = ast.parse(f.read())
        f.close()
        classVisiter = astUtils.ClassNodeLister()
        classVisiter.visit(tree)
        classNodes = classVisiter.getClassNodes()

        myClass = classNodes[2]
        self.assertEqual(myClass.name, "CouplingExample1", "Checking that we found the right class")

        lister = ListVariablesOfType("CouplingExample2", True)
        lister.visit(myClass)
        results = lister.getVariablesList()
        self.assertEqual(len(results),1,"Expecting 1 variable in results")
        self.assertTrue("otherClass" in results, "Looking for otherClass")

    def test_FindingLocalVars(self):
        f = open(self.getPath())
        tree = ast.parse(f.read())
        f.close()
        classVisiter = astUtils.ClassNodeLister()
        classVisiter.visit(tree)
        classNodes = classVisiter.getClassNodes()

        myClass = classNodes[3]
        self.assertEqual(myClass.name, "CouplingExample2", "Checking that we found the right class")

        lister = ListVariablesOfType("CouplingExample1", False)
        lister.visit(myClass)
        results = lister.getVariablesList()
        self.assertEqual(len(results),1,"Expecting 1 variable in results")
        self.assertTrue("localOtherClass" in results, "Looking for localOtherClass")