class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        
        stack = []
        res = [i for i in prices]

        for i in range(len(prices)):
            while stack and prices[stack[-1]] >= prices[i]:
                val = stack.pop()
                res[val] = prices[val] - prices[i]
            stack.append(i)
        
        return res