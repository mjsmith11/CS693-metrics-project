import unittest
import os.path
from ...src.metrics.loc import LinesOfCode

class TestLOC(unittest.TestCase):
    def getPath(self):
        my_path = os.path.abspath(os.path.dirname(__file__))
        return os.path.join(my_path,"../files/sample1.py")

    def test_basics(self):
        obj = LinesOfCode(self.getPath())
        self.assertEqual(obj.countTotalLines(),285,"Total Lines")
        self.assertEqual(obj.countCommentLines(),176,"Comment Lines")
        self.assertEqual(obj.countEmptyLines(),34,"Empty Lines")
        self.assertEqual(obj.countImportLines(),1,"Import Lines")

        
    
    def test_allOff(self):
        obj = LinesOfCode(self.getPath())
        obj.countLines()
        expectedLines = 74
        actualLines = obj.getCount(False, False, False)
        self.assertEqual(actualLines, expectedLines, "line count")

    def test_imports(self):
        obj = LinesOfCode(self.getPath())
        obj.countLines()
        expectedLines = 75
        actualLines = obj.getCount(False, False, True)
        self.assertEqual(actualLines, expectedLines, "line count")

        defaultParamCount = obj.getCount()
        self.assertEqual(defaultParamCount, expectedLines, "line count with default params")

    def test_empty(self):
        obj = LinesOfCode(self.getPath())
        obj.countLines()
        expectedLines = 108
        actualLines = obj.getCount(False, True, False)
        self.assertEqual(actualLines, expectedLines, "line count")

    def test_emptyAndImports(self):
        obj = LinesOfCode(self.getPath())
        obj.countLines()
        expectedLines = 109
        actualLines = obj.getCount(False, True, True)
        self.assertEqual(actualLines, expectedLines, "line count")

    def test_comments(self):
        obj = LinesOfCode(self.getPath())
        obj.countLines()
        expectedLines = 250
        actualLines = obj.getCount(True, False, False)
        self.assertEqual(actualLines, expectedLines, "line count")
    
    def test_commentsAndImports(self):
        obj = LinesOfCode(self.getPath())
        obj.countLines()
        expectedLines = 251
        actualLines = obj.getCount(True, False, True)
        self.assertEqual(actualLines, expectedLines, "line count")

    def test_commentsAndEmpty(self):
        obj = LinesOfCode(self.getPath())
        obj.countLines()
        expectedLines = 284
        actualLines = obj.getCount(True, True, False)
        self.assertEqual(actualLines, expectedLines, "line count")

    def test_allOn(self):
        obj = LinesOfCode(self.getPath())
        obj.countLines()
        expectedLines = 285
        actualLines = obj.getCount(True, True, True)
        self.assertEqual(actualLines, expectedLines, "line count")

