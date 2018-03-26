class LinesOfCode:
    def __init__(self, filepath):
        self.file = filepath

    def countLines(self):
        """ Although this could be accomplished with one pass through the file,
            multiple passes are used for simpler counting methods. Choosing this approach 
            does not change the time complexity of O(n) """
        self.commentLines = self.countCommentLines()
        self.emptyLines = self.countEmptyLines()
        self.importLines = self.countImportLines()
        # anything not in a previous category is a considered a statement
        self.statementLines = self.countTotalLines() - (self.commentLines + self.emptyLines + self.importLines) 

    def getCount(self, comments=False, emptyLines = False, importStatements = False):
        result = self.statementLines
        if comments:
            result += self.commentLines
        if emptyLines:
            result += self.emptyLines
        if importStatements:
            result += self.importLines

    def countCommentLines(self):
        raise NotImplementedError

    def countEmptyLines(self):
        raise NotImplementedError       

    def countImportLines(self):
        raise NotImplementedError

    def countTotalLines(self):
        f = open(self.file, 'r')
        lineCount = 0
        for line in f:
            lineCount += 1
        f.close()
        return lineCount