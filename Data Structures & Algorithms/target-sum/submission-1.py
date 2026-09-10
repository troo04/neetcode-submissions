class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}
        
        def dp(i, total):
            if (i, total) in cache:
                return cache[(i, total)]
            
            if total == target and i == len(nums):
                return 1
            
            if i >= len(nums):
                return 0
            
            cache[(i, total)] = dp(i + 1, total + nums[i]) + dp(i + 1, total - nums[i])
            return cache[(i, total)]
        
        return dp(0, 0)