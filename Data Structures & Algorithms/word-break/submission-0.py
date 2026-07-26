class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        memo = {}

        def recurse(i):
            if i in memo:
                return memo[i]
            
            if i == len(s):
                return True
            
            res = False
            for j in range(i, len(s) + 1):
                if s[i: j] in wordDict:
                    res = res or recurse(j)
            
            memo[i] = res
            return res
        
        return recurse(0)