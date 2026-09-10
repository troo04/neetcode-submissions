class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache = {}
        def dp(i, total):
            if i >= len(coins):
                return 0
            
            if (i, total) in cache:
                return cache[(i, total)]
            
            if total == amount:
                return 1
            
            if total > amount:
                return 0
            
            res = 0
            res = dp(i + 1, total)
            if coins[i] + total <= amount:
                res += dp(i, total + coins[i])
            
            cache[(i, total)] = res
            return res
        
        return dp(0, 0)