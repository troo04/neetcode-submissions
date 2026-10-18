class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        if len(s) < len(p):
            return []
        
        p_char = {}

        for i in range(len(p)):
            if p[i] not in p_char:
                p_char[p[i]] = 1
            else:
                p_char[p[i]] += 1
        
        window = {}

        res = []

        for i in range(len(p)):
            if s[i] not in window:
                window[s[i]] = 1
            else:
                window[s[i]] += 1
        
        if window == p_char:
            res.append(0)

        for j in range(len(p), len(s)):
            if s[j] in window:
                window[s[j]] += 1
            else:
                window[s[j]] = 1
            
            window[s[j - len(p)]] -= 1

            if window[s[j - len(p)]] == 0:
                del window[s[j - len(p)]]
            
            if window == p_char:
                res.append(j - len(p) + 1)
        
        return res