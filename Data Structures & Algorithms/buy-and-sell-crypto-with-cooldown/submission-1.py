class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cache = {}
        def dp(i, state):
            if (i, state) in cache:
                return cache[(i, state)]
            
            if i >= len(prices):
                return 0
            
            if state == "B":
                cache[(i, state)] = max(dp(i + 1, "S") - prices[i], dp(i + 1, "B"))
            else:
                cache[(i, state)] = max(dp(i + 2, "B") + prices[i], dp(i + 1, "S"))
            
            return cache[(i, state)]
        
        return dp(0, "B")