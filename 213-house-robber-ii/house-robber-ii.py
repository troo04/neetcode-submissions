class Solution:
    def rob(self, nums: list[int]) -> int:
        cache = {}

        def dp(i, robbedFirst):

            if (i, robbedFirst) in cache:
                return cache[(i, robbedFirst)]

            if i >= len(nums):
                return 0
            
            if i == len(nums) - 1 and robbedFirst:
                return 0
            
            if i == 0:
                cache[(i, robbedFirst)] = max(nums[i] + dp(i + 2, True), dp(i + 1, False))
            else:
                cache[(i, robbedFirst)] = max(nums[i] + dp(i + 2, robbedFirst), dp(i + 1, robbedFirst))
            
            return cache[(i, robbedFirst)]
        
        return dp(0, False)