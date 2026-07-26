class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dp(amt):
            if amt in memo:
                return memo[amt]
            
            if amt == 0:
                return 0
            
            res = float('inf')
            for coin in coins:
                if amt >= coin:
                    res = min(res, 1 + dp(amt - coin))
            
            memo[amt] = res
            return res
        
        minCoins = dp(amount)
        if minCoins == float('inf'):
            return -1
        return minCoins