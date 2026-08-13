import re

class Spreadsheet:

    def __init__(self, rows: int):
        self.spreadsheet = [[0 for _ in range(26)] for _ in range(rows)]

    def setCell(self, cell: str, value: int) -> None:
        col, row = ord(cell[0]) - ord('A'), int(cell[1:]) - 1

        self.spreadsheet[row][col] = value

    def resetCell(self, cell: str) -> None:
        col, row = ord(cell[0]) - ord('A'), int(cell[1:]) - 1

        self.spreadsheet[row][col] = 0

    def getValue(self, formula: str) -> int:
        cells = [c for c in re.split(r"[=+]", formula) if c]

        res = 0
        if ord('A') <= ord(cells[0][0]) <= ord('Z'):
            col, row = ord(cells[0][0]) - ord('A'), int(cells[0][1:]) - 1
            res += self.spreadsheet[row][col]
        else:
            res += int(cells[0])

        if ord('A') <= ord(cells[1][0]) <= ord('Z'):
            col, row = ord(cells[1][0]) - ord('A'), int(cells[1][1:]) - 1
            res += self.spreadsheet[row][col]
        else:
            res += int(cells[1])
        
        return res

# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)