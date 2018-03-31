import unittest
import sys
sys.path.append('../../src/metrics')
from loc import LinesOfCode

class TestLOC(unittest.TestCase):
    def test_basics(self):
        obj = LinesOfCode("../files/sample1.py")
        self.assertEqual(obj.countTotalLines(),283,"Total Lines")
        self.assertEqual(obj.countCommentLines(),176,"Comment Lines")
        self.assertEqual(obj.countEmptyLines(),34,"Empty Lines")
        self.assertEqual(obj.countImportLines(),1,"Import Lines")

        
    
    def test_allOff(self):
        obj = LinesOfCode("../files/sample1.py")
        obj.countLines()
        expectedLines = 72
        actualLines = obj.getCount(False, False, False)
        self.assertEqual(actualLines, expectedLines, "line count")

    def test_imports(self):
        obj = LinesOfCode("../files/sample1.py")
        obj.countLines()
        expectedLines = 73
        actualLines = obj.getCount(False, False, True)
        self.assertEqual(actualLines, expectedLines, "line count")

        defaultParamCount = obj.getCount()
        self.assertEqual(defaultParamCount, expectedLines, "line count with default params")

    def test_empty(self):
        obj = LinesOfCode("../files/sample1.py")
        obj.countLines()
        expectedLines = 106
        actualLines = obj.getCount(False, True, False)
        self.assertEqual(actualLines, expectedLines, "line count")

    def test_emptyAndImports(self):
        obj = LinesOfCode("../files/sample1.py")
        obj.countLines()
        expectedLines = 107
        actualLines = obj.getCount(False, True, True)
        self.assertEqual(actualLines, expectedLines, "line count")

    def test_comments(self):
        obj = LinesOfCode("../files/sample1.py")
        obj.countLines()
        expectedLines = 248
        actualLines = obj.getCount(True, False, False)
        self.assertEqual(actualLines, expectedLines, "line count")
    
    def test_commentsAndImports(self):
        obj = LinesOfCode("../files/sample1.py")
        obj.countLines()
        expectedLines = 249
        actualLines = obj.getCount(True, False, True)
        self.assertEqual(actualLines, expectedLines, "line count")

    def test_commentsAndEmpty(self):
        obj = LinesOfCode("../files/sample1.py")
        obj.countLines()
        expectedLines = 282
        actualLines = obj.getCount(True, True, False)
        self.assertEqual(actualLines, expectedLines, "line count")

    def test_allOn(self):
        obj = LinesOfCode("../files/sample1.py")
        obj.countLines()
        expectedLines = 283
        actualLines = obj.getCount(True, True, True)
        self.assertEqual(actualLines, expectedLines, "line count")

if __name__ == '__main__':
    unittest.main()
