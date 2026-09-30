class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        memo = {}

        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            
            res = 1
            
            for d in dirs:
                new_i, new_j = i + d[0], j + d[1]

                if new_i >= 0 and new_i < len(matrix) and new_j >= 0 and new_j < len(matrix[0]) and matrix[new_i][new_j] > matrix[i][j]:
                    res = max(res, 1 + dp(new_i, new_j))
            
            memo[(i, j)] = res
            return res
        
        res = 0

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                res = max(res, dp(i, j))
        
        return res