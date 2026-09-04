class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        columnCounter = [{} for x in range(9)]
        boxCounter = [{} for x in range(3)]
        rowCounter = {}

        for i in range(len(board)):
            row = board[i]

            for a in range(len(row)):
                rowCounter[row[a]] = 1 + rowCounter.get(row[a],0) #logic for row count
                
                columnCounter[a][row[a]] = 1 + columnCounter[a].get(row[a],0) #logic for column count

                boxCounter[int(a/3)][row[a]] = 1 + boxCounter[int(a/3)].get(row[a],0)

                if (rowCounter[row[a]] > 1 or columnCounter[a][row[a]] > 1 or boxCounter[int(a/3)][row[a]] > 1 ) and row[a] != ".":
                    return False
            
            if (i+1) % 3 == 0:
                boxCounter = [{} for x in range(3)]
            rowCounter = {}
        return True