class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        cache = {}

        def dp(i, total1, total2):
            if (i, total1, total2) in cache:
                return cache[(i, total1, total2)]
            
            if total1 == total2 and i >= len(nums):
                return True
            
            if i >= len(nums):
                return False
            
            cache[(i, total1, total2)] = dp(i + 1, total1 + nums[i], total2) or dp(i + 1, total1, total2 + nums[i])

            return cache[(i, total1, total2)]
        
        return dp(0, 0, 0)