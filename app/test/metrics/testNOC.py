import unittest
import os.path
from ...src.metrics.noc import NOC

class testNOC(unittest.TestCase):
    def getPath(self):
        my_path = os.path.abspath(os.path.dirname(__file__))
        return os.path.join(my_path,"../files/sample1.py")

    def test_Calculation(self):
        noc = NOC(self.getPath())
        results = noc.calculateAll()
        self.assertEqual(len(results),11,"Number of Results")
        self.assertEqual(results["CohesionExample1"], 0, "CohesionExample1 result")
        self.assertEqual(results["CohesionExample2"], 0, "CohesionExample2 result")
        self.assertEqual(results["CouplingExample1"], 0, "CouplingExample1 result")
        self.assertEqual(results["CouplingExample2"], 0, "CouplingExample2 result")
        self.assertEqual(results["DepthOfInheritanceExample1"], 1, "DepthOfInheritanceExample1 result")
        self.assertEqual(results["DepthOfInheritanceExample2"], 0, "DepthOfInheritanceExample2 result")
        self.assertEqual(results["DepthOfInheritanceExample3"], 1, "DepthOfInheritanceExample3 result")
        self.assertEqual(results["DepthOfInheritanceExample4"], 0, "DepthOfInheritanceExample4 result")
        self.assertEqual(results["NumberOfChildrenExample1"], 2, "NumberOfChildrenExample1 result")
        self.assertEqual(results["NumberOfChildrenExample2"], 0, "NumberOfChildrenExample2 result")
        self.assertEqual(results["NumberOfChildrenExample3"], 0, "NumberOfChildrenExample3 result")
