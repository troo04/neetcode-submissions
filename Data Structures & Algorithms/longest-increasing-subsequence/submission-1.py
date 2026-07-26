class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        memo = {}
        def dp(i, prevMax):
            if (i, prevMax) in memo:
                return memo[(i, prevMax)]
            
            if i >= len(nums):
                return 0
            
            res = float('-inf')
            if nums[i] > prevMax:
                res = 1 + dp(i + 1, nums[i])
            
            res = max(res, dp(i + 1, prevMax))
            memo[(i, prevMax)] = res
            
            return res
        
        return dp(0, float('-inf'))