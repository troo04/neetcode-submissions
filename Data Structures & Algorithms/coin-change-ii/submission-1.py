class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache = {}
        def dp(i, total):
            if (i, total) in cache:
                return cache[(i, total)]
            
            if total == amount:
                return 1
            
            if total > amount:
                return 0
            
            res = 0
            for j in range(i, len(coins)):
                res += dp(j, total + coins[j])
            
            cache[(i, total)] = res
            return res
        
        return dp(0, 0)