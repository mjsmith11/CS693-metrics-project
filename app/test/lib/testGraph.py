import unittest
import sys
from ...src.lib.graph import Graph

class TestGraph(unittest.TestCase):
    def test_createUnGraph(self):
        g = Graph(False)
        g.add_edge("A","B") #two new nodes
        g.add_edge("B","C") #old/new
        g.add_edge("D","B") #new/old
        g.add_edge("D","A") #old/old
        g.add_node("E")     #disconnected node

        self.assertTrue(g.nodeExists("A"), "node A should exist")
        self.assertTrue(g.nodeExists("B"), "node B should exist")
        self.assertTrue(g.nodeExists("C"), "node C should exist")
        self.assertTrue(g.nodeExists("D"), "node D should exist")
        self.assertTrue(g.nodeExists("E"), "node E should exist")
        self.assertEqual(len(g.graph), 5, "graph should have 5 nodes")

        #A => B,D
        #B => A,C,D
        #C => B
        #D => B,A
        #E =>

        self.assertEqual(len(g.graph["A"]), 2, "Number of Neighbors to A")
        self.assertEqual(len(g.graph["B"]), 3, "Number of Neighbors to B")
        self.assertEqual(len(g.graph["C"]), 1, "Number of Neighbors to C")
        self.assertEqual(len(g.graph["D"]), 2, "Number of Neighbors to D")
        self.assertEqual(len(g.graph["E"]), 0, "Number of Neighbors to E")

        self.assertTrue("B" in g.graph["A"], "B should be A's neighbor")
        self.assertTrue("D" in g.graph["A"], "D should be A's neighbor")
        self.assertTrue("A" in g.graph["B"], "A should be B's neighbor")
        self.assertTrue("C" in g.graph["B"], "C should be B's neighbor")
        self.assertTrue("D" in g.graph["B"], "D should be B's neighbor")
        self.assertTrue("B" in g.graph["C"], "B should be C's neighbor")
        self.assertTrue("B" in g.graph["D"], "B should be D's neighbor")
        self.assertTrue("A" in g.graph["D"], "A should be D's neighbor")

    def test_createDiGraph(self):
        g = Graph(True)
        g.add_edge("A","B") #two new nodes
        g.add_edge("B","C") #old/new
        g.add_edge("D","B") #new/old
        g.add_edge("D","A") #old/old
        g.add_node("E")     #disconnected node

        self.assertTrue(g.nodeExists("A"), "node A should exist")
        self.assertTrue(g.nodeExists("B"), "node B should exist")
        self.assertTrue(g.nodeExists("C"), "node C should exist")
        self.assertTrue(g.nodeExists("D"), "node D should exist")
        self.assertTrue(g.nodeExists("E"), "node E should exist")
        self.assertEqual(len(g.graph), 5, "graph should have 5 nodes")

        #A => B
        #B => C
        #C => 
        #D => B, A
        #E =>

        self.assertEqual(len(g.graph["A"]), 1, "Number of Neighbors to A")
        self.assertEqual(len(g.graph["B"]), 1, "Number of Neighbors to B")
        self.assertEqual(len(g.graph["C"]), 0, "Number of Neighbors to C")
        self.assertEqual(len(g.graph["D"]), 2, "Number of Neighbors to D")
        self.assertEqual(len(g.graph["E"]), 0, "Number of Neighbors to E")

        self.assertTrue("B" in g.graph["A"], "B should be A's neighbor")
        self.assertTrue("B" in g.graph["D"], "B should be D's neighbor")
        self.assertTrue("A" in g.graph["D"], "A should be D's neighbor")   

    def test_SingleConnectedComponent(self):
        g = Graph()
        g.add_edge("A","B")
        g.add_edge("B","x")
        g.add_edge("C","x")
        g.add_edge("C","y")
        g.add_edge("D","y")
        g.add_edge("D","E")

        self.assertEqual(g.countConnectedComponents(), 1, "Incorrect count")   

    def test_TwoConnectedComponents(self):
        g = Graph()
        g.add_edge("A","B")
        g.add_edge("B","x")
        g.add_edge("C","y")
        g.add_edge("D","y")
        g.add_edge("D","E")

        self.assertEqual(g.countConnectedComponents(), 2, "Incorrect count")   
