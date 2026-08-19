class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        perm = {}
        window = {}

        for i in range(len(s1)):
            if s2[i] in window:
                window[s2[i]] += 1
            else:
                window[s2[i]] = 1
            
            if s1[i] in perm:
                perm[s1[i]] += 1
            else:
                perm[s1[i]] = 1
        
        for i in range(len(s2) - len(s1) + 1):
            print(window)
            if window == perm:
                return True
            
            window[s2[i]] -= 1

            if window[s2[i]] == 0:
                del window[s2[i]]
            
            if i + len(s1) < len(s2) and s2[i + len(s1)] in window:
                window[s2[i + len(s1)]] += 1
            elif i + len(s1) < len(s2):
                window[s2[i + len(s1)]] = 1
            
        return False