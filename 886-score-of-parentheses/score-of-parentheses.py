class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        depth = 0
        score = 0

        for i in range(len(s)):
            if s[i] == '(':
                depth += 1
            else:
                if s[i - 1] == '(':
                    score += 2 ** (depth - 1)
                
                depth -= 1
        
        return score