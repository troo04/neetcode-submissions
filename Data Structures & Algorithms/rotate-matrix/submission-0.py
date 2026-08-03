class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        ## transpose a matrix

        for i in range(len(matrix)):
            for j in range(i, len(matrix[0])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        ## swap

        for i in range(len(matrix)):
            for j in range(math.ceil(len(matrix[0]) // 2)):
                matrix[i][j], matrix[i][len(matrix[0]) - j - 1] =  matrix[i][len(matrix[0]) - j - 1], matrix[i][j]