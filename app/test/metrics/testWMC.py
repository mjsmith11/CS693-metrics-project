import unittest
import os.path
from ...src.metrics.wmc import WMC

class testWMC(unittest.TestCase):
    def getPath(self):
        my_path = os.path.abspath(os.path.dirname(__file__))
        return os.path.join(my_path,"../files/sample1.py")

    def test_CalculationWithoutInit(self):
        wmc = WMC(self.getPath())
        results = wmc.calculateAll(False)
        self.assertEqual(len(results),11,"Number of Results")
        self.assertEqual(results["CohesionExample1"], 5, "CohesionExample1 result")
        self.assertEqual(results["CohesionExample2"], 5, "CohesionExample2 result")
        self.assertEqual(results["CouplingExample1"], 1, "CouplingExample1 result")
        self.assertEqual(results["CouplingExample2"], 1, "CouplingExample2 result")
        self.assertEqual(results["DepthOfInheritanceExample1"], 0, "DepthOfInheritanceExample1 result")
        self.assertEqual(results["DepthOfInheritanceExample2"], 0, "DepthOfInheritanceExample2 result")
        self.assertEqual(results["DepthOfInheritanceExample3"], 0, "DepthOfInheritanceExample3 result")
        self.assertEqual(results["DepthOfInheritanceExample4"], 0, "DepthOfInheritanceExample4 result")
        self.assertEqual(results["NumberOfChildrenExample1"], 0, "NumberOfChildrenExample1 result")
        self.assertEqual(results["NumberOfChildrenExample2"], 0, "NumberOfChildrenExample2 result")
        self.assertEqual(results["NumberOfChildrenExample3"], 0, "NumberOfChildrenExample3 result")

    def test_CalculationWithInit(self):
        wmc = WMC(self.getPath())
        results = wmc.calculateAll(True)
        self.assertEqual(len(results),11,"Number of Results")
        self.assertEqual(results["CohesionExample1"], 6, "CohesionExample1 result")
        self.assertEqual(results["CohesionExample2"], 6, "CohesionExample2 result")
        self.assertEqual(results["CouplingExample1"], 2, "CouplingExample1 result")
        self.assertEqual(results["CouplingExample2"], 2, "CouplingExample2 result")
        self.assertEqual(results["DepthOfInheritanceExample1"], 1, "DepthOfInheritanceExample1 result")
        self.assertEqual(results["DepthOfInheritanceExample2"], 1, "DepthOfInheritanceExample2 result")
        self.assertEqual(results["DepthOfInheritanceExample3"], 1, "DepthOfInheritanceExample3 result")
        self.assertEqual(results["DepthOfInheritanceExample4"], 1, "DepthOfInheritanceExample4 result")
        self.assertEqual(results["NumberOfChildrenExample1"], 1, "NumberOfChildrenExample1 result")
        self.assertEqual(results["NumberOfChildrenExample2"], 1, "NumberOfChildrenExample2 result")
        self.assertEqual(results["NumberOfChildrenExample3"], 1, "NumberOfChildrenExample3 result")