class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]

        cache = {}

        def dp(left, right):
            if (left, right) in cache:
                return cache[(left, right)]

            if left > right:
                return 0
            
            res = 0
            for i in range(left, right + 1):
                ## we treat it like this is the last balloon to pop so that that way we can use the left and right side as boundaries since everything else is popped away
                coins = nums[left - 1] * nums[i] * nums[right + 1]

                res = max(res, coins + dp(left, i - 1) + dp(i + 1, right))
            
            cache[(left, right)] = res
            return res


        return dp(1, len(nums) - 2)