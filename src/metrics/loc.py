class loc:
    def __init__(self,filepath):
        self.file = filepath

    def countLines():
        """ Although this could be accomplished with one pass through the file,
            multiple passes are used for simpler counting methods. Choosing this approach 
            does not change the time complexity of O(n) """
        self.commentLines = self.countCommentLines()
        self.emptyLines = self.countEmptyLines()
        self.importLines = self.countImportLines()
        # anything not in a previous category is a considered a statement
        self.statementLines = self.countTotalLines() - (self.commentLines + self.emptyLines + self.importLines) 

    def getCount(comments=False, emptyLines = False, importStatements = False):
        result = self.statementLines
        if comments:
            result += self.commentLines
        if emptyLines:
            result += self.emptyLines
        if importStatements:
            result += self.importLines

    def countCommentLines():
        raise NotImplementedError

    def countEmptyLines():
        raise NotImplementedError       

    def countImportLines():
        raise NotImplementedError

    def countTotalLines():
        raise NotImplementedError