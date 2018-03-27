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
        return result
     
    def countCommentLines(self):
        f = open(self.file, 'r')
        count = 0
        inCommentBlock = False
        tripleQuote = "\"\"\""
        for line in f:
            line = line.strip()

            #single line comment (lines with a statement and # comment don't count)
            if(line.startswith("#") and not inCommentBlock):
                count += 1
                continue

            #block comments
            if(inCommentBlock):
                if(line.endswith(tripleQuote)):
                    #end of block comment and this whole line is part of the comment
                    count += 1
                    inCommentBlock = False
                elif(tripleQuote in line):
                    #comment block ends but there is something after it. This line doesn't count
                    inCommentBlock = False
                else:
                    #A line in the middle of the block comment
                    count += 1
            else:
                if(line.startswith(tripleQuote)):
                    #starting a block comment and this whole line is part of the comment
                    inCommentBlock = True
                    count += 1
                elif(tripleQuote in line):
                    #block comment starts partway through this line.  This line doesn't count
                    inCommentBlock = True
        f.close()
        return count


    def countEmptyLines(self):
        f = open(self.file, 'r')
        count = 0
        for line in f:
            # strip removes whitespace from beginning and end of string. String is false if it is ""
            if(not line.strip()): 
                count += 1
        f.close()
        return count     

    def countImportLines(self):
        f = open(self.file, 'r')
        count = 0
        for line in f:
            line = line.strip()
            pieces = line.split(" ")
            if(pieces[0] == "import"):
                count += 1
            elif((pieces[0] == "from") and (pieces[2] == "import")):
                count += 1
        f.close()
        return count

    def countTotalLines(self):
        f = open(self.file, 'r')
        lineCount = 0
        for line in f:
            lineCount += 1
        f.close()
        return lineCount