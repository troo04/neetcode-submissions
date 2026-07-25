class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        longest = 0
        subs = ""

        for i in range(len(s)):
            ## even
            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > longest:
                    longest = right - left + 1
                    subs = s[left: right + 1]
                
                left -= 1
                right += 1
            
            ## odd
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > longest:
                    longest = right - left + 1
                    subs = s[left: right + 1]
                
                left -= 1
                right += 1
        
        return subs