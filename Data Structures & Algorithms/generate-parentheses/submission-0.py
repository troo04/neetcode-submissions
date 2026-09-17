class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def generate(rem_left, rem_right, combo):
            if rem_left == 0 and rem_right == 0:
                res.append(combo)
                return
            
            if rem_left > 0:
                generate(rem_left - 1, rem_right, combo + "(")
            
            if rem_left < rem_right:
                generate(rem_left, rem_right - 1, combo + ")")
        
        generate(n, n, "")
        return res