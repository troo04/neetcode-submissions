
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        cache = {}
        
        def dp(i, j):
            if (i, j) in cache:
                return cache[(i, j)]

            if j == len(p):
                return i == len(s)
            
            match = i < len(s) and (s[i] == p[j] or (p[j] == "."))

            res = False
            if j + 1 < len(p) and p[j + 1] == "*":
                res = dp(i, j + 2)
                res = res or (match and dp(i + 1, j))
            
            if match:
                res = res or dp(i + 1, j + 1)
            
            cache[(i, j)] = res
            return res
        
        return dp(0, 0)