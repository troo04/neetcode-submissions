class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {len(s) : 1}

        def dp(i):
            if i in memo:
                return memo[i]
            
            if s[i] == "0":
                return 0

            else:
                count = 0
                if 1 <= int(s[i]) <= 26:
                    count += dp(i + 1)
                if i + 1 < len(s) and 1 <= int(s[i: i + 2]) <= 26:
                    count += dp(i + 2)

                memo[i] = count
                return memo[i]
    
        return dp(0)