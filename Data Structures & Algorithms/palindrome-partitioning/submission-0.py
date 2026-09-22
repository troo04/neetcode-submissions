class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []

        def dp(start):
            if start == len(s):
                res.append(part[::])
                return
            
            for end in range(start, len(s)):
                if self.isPali(s, start, end):
                    part.append(s[start : end + 1])
                    dp(end + 1)
                    part.pop()
            
        dp(0)
        return res
    
    def isPali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True