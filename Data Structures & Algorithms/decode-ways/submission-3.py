class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}

        def dp(substr):
            if substr in memo:
                return memo[substr]
            if len(substr) < 1:
                memo[substr] = 1
                return memo[substr]
            
            if len(substr) == 1:
                if substr[0] == "0":
                    memo[substr] = 0
                    return memo[substr]
                else:
                    memo[substr] = 1
                    return memo[substr]
            
            if substr[0] == "0":
                memo[substr] = 0
                return memo[substr]
            else:
                count = 0
                if 1 <= int(substr[0]) <= 26:
                    count += dp(substr[1:])
                if 1 <= int(substr[0:2]) <= 26:
                    count += dp(substr[2:])

                memo[substr] = count
                return memo[substr]
    
        return dp(s)