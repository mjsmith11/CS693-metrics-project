class LinesOfCode:
    TRIPLE_QUOTE = "\"\"\""

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

    def getCount(self, comments=False, emptyLines = False, importStatements = True):
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
        for line in f:
            line = line.strip()

            #single line comment (lines with a statement and # comment don't count)
            if(line.startswith("#") and not inCommentBlock):
                count += 1
                continue

            #block comments
            if(inCommentBlock):
                if(line.endswith(self.TRIPLE_QUOTE)):
                    #end of block comment and this whole line is part of the comment
                    count += 1
                    inCommentBlock = False
                else:
                    #A line in the middle of the block comment
                    count += 1
            else:
                if(line.startswith(self.TRIPLE_QUOTE) and line.endswith(self.TRIPLE_QUOTE) and len(line)>5):
                    #single line block comment. Note 3,4,or 5 quotes satisfy the first two conditions but only open the comment. It is not closed
                    count += 1
                elif(line.startswith(self.TRIPLE_QUOTE)):
                    #starting a block comment and this whole line is part of the comment
                    inCommentBlock = True
                    count += 1
        f.close()
        return count


    def countEmptyLines(self):
        f = open(self.file, 'r')
        count = 0
        inCommentBlock = False
        for line in f:
            if(line.startswith(self.TRIPLE_QUOTE)):
                inCommentBlock = not inCommentBlock
            if(line.endswith(self.TRIPLE_QUOTE)):
                inCommentBlock = not inCommentBlock
            # strip removes whitespace from beginning and end of string. String is false if it is ""
            if(not (line.strip() or inCommentBlock)): 
                count += 1
        f.close()
        return count     

    def countImportLines(self):
        f = open(self.file, 'r')
        count = 0
        inCommentBlock = False
        for line in f:
            line = line.strip()
            if (inCommentBlock):
                if (line.endswith(self.TRIPLE_QUOTE)):
                    inCommentBlock = False
            else:
                if(line.startswith(self.TRIPLE_QUOTE) and line.endswith(self.TRIPLE_QUOTE) and len(line)>5):
                    #single line block comment. Note 3,4,or 5 quotes satisfy the first two conditions but only open the comment. It is not closed
                    pass
                elif (line.startswith(self.TRIPLE_QUOTE)):
                    inCommentBlock = True
                elif (self.isImport(line)):
                    count += 1
        f.close()
        return count

    def isImport(self, line):
        pieces = line.split(" ")
        if(pieces[0] == "import"):
            return True
        elif((pieces[0] == "from") and (pieces[2] == "import")):
            return True
        return False


    def countTotalLines(self):
        f = open(self.file, 'r')
        lineCount = 0
        for _ in f:
            lineCount += 1
        f.close()
        return lineCount