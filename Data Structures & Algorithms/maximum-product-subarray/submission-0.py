class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curMin, curMax = 1, 1

        for num in nums:
            tmp = curMax * num

            curMax = max(num, tmp, curMin * num)
            curMin = min(num, tmp, curMin * num)
            res = max(res, curMax)
        
        return res
