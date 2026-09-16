class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cache = {}
        def dp(i, state, total):
            if (i, state, total) in cache:
                return cache[(i, state, total)]
            
            if i >= len(prices):
                return total
            
            if state == "B":
                cache[(i, state, total)] = max(dp(i + 1, "S", total - prices[i]), dp(i + 1, "B", total))
            else:
                cache[(i, state, total)] = max(dp(i + 2, "B", total + prices[i]), dp(i + 1, "S", total))
            
            return cache[(i, state, total)]
        
        return dp(0, "B", 0)