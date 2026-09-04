class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.boards = []

        def checkValidPos(board, row, col):
            ## check left/right diagonal
            i, j = row, col
            while i >= 0 and j < len(board):
                if board[i][j] == "Q":
                    return False
                i -= 1
                j += 1
            
            i, j = row, col
            while i >= 0 and j >= 0:
                if board[i][j] == "Q":
                    return False
                i -= 1
                j -= 1
            
            i, j = row, col
            while i < len(board) and j < len(board):
                if board[i][j] == "Q":
                    return False
                i += 1
                j += 1
            
            i, j = row, col
            while i < len(board) and j >= 0:
                if board[i][j] == "Q":
                    return False
                i += 1
                j -= 1
            
            ## check the col
            i, j = 0, col
            while i < len(board):
                if board[i][j] == "Q":
                    return False
                i += 1
            
            return True

        def findValidArrangement(board, row):
            if row == n:
                ## condense row before appending
                self.boards.append(["".join(r) for r in board])
                return
            
            for i in range(n):
                if checkValidPos(board, row, i):
                    board[row][i] = "Q"
                    findValidArrangement([r.copy() for r in board], row + 1)
                    board[row][i] = "."
            
            return
        
        ## create an empty board
        board = [["." for _ in range(n)] for _ in range(n)]
        findValidArrangement(board, 0)
        return self.boards