
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        cache = {}
        
        def dp(i, j):
            if (i, j) in cache:
                return cache[(i, j)]

            ## if we have reached the end of pattern then we just gotta see if we made it past i
            if j == len(p):
                return i == len(s)
            
            ## see if the current two letters match
            match = i < len(s) and (s[i] == p[j] or (p[j] == "."))

            res = False
            
            ## if there is a wildcard then skip it or use it (if theres a match)
            if j + 1 < len(p) and p[j + 1] == "*":
                ## skip
                res = dp(i, j + 2)

                ## use
                if match:
                    res = res or dp(i + 1, j)
            
            if match:
                res = res or dp(i + 1, j + 1)
            
            cache[(i, j)] = res
            return res
        
        return dp(0, 0)