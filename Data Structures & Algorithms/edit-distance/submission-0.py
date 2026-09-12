class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        cache = {}
        def dp(i, j):
            if (i, j) in cache:
                return cache[(i, j)]
            
            if i == len(word1) and j == len(word2):
                return 0
            
            minimum = float('inf')
            if i == len(word1):
                minimum = min(minimum, 1 + dp(i, j + 1))
            elif j == len(word2):
                minimum = min(minimum, 1 + dp(i + 1, j))
            elif word1[i] == word2[j]:
                minimum = min(minimum, dp(i + 1, j + 1))
            else:
                ## insert
                minimum = min(minimum, 1 + dp(i, j + 1))
                ## delete
                minimum = min(minimum, 1 + dp(i + 1, j))
                ## replace
                minimum = min(minimum, 1 + dp(i + 1, j + 1))

            cache[(i, j)] = minimum
            return cache[(i, j)]
        
        return dp(0, 0)