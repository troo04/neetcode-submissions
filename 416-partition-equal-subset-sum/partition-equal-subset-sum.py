class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        
        cache = {}
        target = sum(nums) // 2
        def dp(i, total):
            if (i, total) in cache:
                return cache[(i, total)]
            
            if total == target:
                return True
            
            if i >= len(nums):
                return False
            
            cache[(i, total)] = dp(i + 1, total + nums[i]) or dp(i + 1, total)

            return cache[(i, total)]
        
        return dp(0, 0)