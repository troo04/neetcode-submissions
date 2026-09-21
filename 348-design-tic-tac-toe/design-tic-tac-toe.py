class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.rows_1 = [0] * n
        self.cols_1 = [0] * n
        self.diag_1 = 0
        self.anti_1 = 0

        self.rows_2 = [0] * n
        self.cols_2 = [0] * n
        self.diag_2 = 0
        self.anti_2 = 0

    def move(self, row: int, col: int, player: int) -> int:
        if player == 1:
            self.rows_1[row] += 1
            self.cols_1[col] += 1
            
            if self.rows_1[row] == self.n or self.cols_1[col] == self.n:
                return 1
            
            if row == col:
                self.diag_1 += 1
            
            if col == len(self.cols_1) - row - 1:
                self.anti_1 += 1

            if self.diag_1 == self.n:
                return 1
            
            if self.anti_1 == self.n:
                return 1
        else:
            self.rows_2[row] += 1
            self.cols_2[col] += 1
            
            if self.rows_2[row] == self.n or self.cols_2[col] == self.n:
                return 2
            
            if row == col:
                self.diag_2 += 1
            
            if col == len(self.cols_2) - row - 1:
                self.anti_2 += 1

            if self.diag_2 == self.n:
                return 2
            
            if self.anti_2 == self.n:
                return 2
        
        return 0
            


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)