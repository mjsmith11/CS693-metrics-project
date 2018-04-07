import unittest
import os.path
from ...src.metrics.dit import DIT

class testDIT(unittest.TestCase):
    def getPath(self):
        my_path = os.path.abspath(os.path.dirname(__file__))
        return os.path.join(my_path,"../files/sample1.py")

    def test_CalculationWithoutObject(self):
        dit = DIT(self.getPath())
        results = dit.calculateAll(False)
        self.assertEqual(len(results),11,"Number of Results")
        self.assertEqual(results["CohesionExample1"], 0, "CohesionExample1 result")
        self.assertEqual(results["CohesionExample2"], 0, "CohesionExample2 result")
        self.assertEqual(results["CouplingExample1"], 0, "CouplingExample1 result")
        self.assertEqual(results["CouplingExample2"], 0, "CouplingExample2 result")
        self.assertEqual(results["DepthOfInheritanceExample1"], 0, "DepthOfInheritanceExample1 result")
        self.assertEqual(results["DepthOfInheritanceExample2"], 1, "DepthOfInheritanceExample2 result")
        self.assertEqual(results["DepthOfInheritanceExample3"], 0, "DepthOfInheritanceExample3 result")
        self.assertEqual(results["DepthOfInheritanceExample4"], 1, "DepthOfInheritanceExample4 result")
        self.assertEqual(results["NumberOfChildrenExample1"], 0, "NumberOfChildrenExample1 result")
        self.assertEqual(results["NumberOfChildrenExample2"], 1, "NumberOfChildrenExample2 result")
        self.assertEqual(results["NumberOfChildrenExample3"], 1, "NumberOfChildrenExample3 result")

    def test_CalculationWithObject(self):
        dit = DIT(self.getPath())
        results = dit.calculateAll(True)
        self.assertEqual(len(results),11,"Number of Results")
        self.assertEqual(results["CohesionExample1"], 0, "CohesionExample1 result")
        self.assertEqual(results["CohesionExample2"], 0, "CohesionExample2 result")
        self.assertEqual(results["CouplingExample1"], 0, "CouplingExample1 result")
        self.assertEqual(results["CouplingExample2"], 0, "CouplingExample2 result")
        self.assertEqual(results["DepthOfInheritanceExample1"], 1, "DepthOfInheritanceExample1 result")
        self.assertEqual(results["DepthOfInheritanceExample2"], 2, "DepthOfInheritanceExample2 result")
        self.assertEqual(results["DepthOfInheritanceExample3"], 0, "DepthOfInheritanceExample3 result")
        self.assertEqual(results["DepthOfInheritanceExample4"], 1, "DepthOfInheritanceExample4 result")
        self.assertEqual(results["NumberOfChildrenExample1"], 0, "NumberOfChildrenExample1 result")
        self.assertEqual(results["NumberOfChildrenExample2"], 1, "NumberOfChildrenExample2 result")
        self.assertEqual(results["NumberOfChildrenExample3"], 1, "NumberOfChildrenExample3 result")