class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ## check the boxes
        
        i, j = 0, 0
        for a in range(3):
            for b in range(3):
                numbers = set()
                temp_j = j

                for x in range(0, 3):
                    for y in range(0, 3):
                        if board[i + x][j + y] in numbers:
                            return False
                        
                        if board[i + x][j + y] != ".":
                            numbers.add(board[i + x][j + y])
            
                j += 3
            j = 0
            i += 3
        
        ## check the rows
        for i in range(len(board)):
            numbers = set()

            for j in range(len(board[0])):
                if board[i][j] in numbers:
                    return False
                    
                if board[i][j] != ".":
                    numbers.add(board[i][j])
        
        ## check the cols
        for j in range(len(board[0])):
            numbers = set()

            for i in range(len(board)):
                if board[i][j] in numbers:
                    return False
                    
                if board[i][j] != ".":
                    numbers.add(board[i][j])
            
        return True