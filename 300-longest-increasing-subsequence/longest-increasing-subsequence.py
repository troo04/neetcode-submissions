class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        cache = {}

        def dp(i):
            if i in cache:
                return cache[i]
            
            if i == len(nums):
                return 0
            
            res = 1
            for j in range(i, len(nums)):
                if nums[j] > nums[i]:
                    res = max(res, 1 + dp(j))

            cache[i] = res
            return res
        
        return max([dp(i) for i in range(len(nums))])