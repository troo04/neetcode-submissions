class Solution:
    def rob(self, nums: List[int], colors: List[int]) -> int:
        memo = {}
        def dp(i, color_code):
            if (i, color_code) in memo:
                return memo[(i, color_code)]
            
            if i >= len(nums):
                return 0
            
            if colors[i] == color_code:
                memo[(i, color_code)] = dp(i + 1, 0)
                return memo[(i, color_code)]
            
            memo[(i, color_code)] = max(nums[i] + dp(i + 1, colors[i]), dp(i + 1, 0))
            return memo[(i, color_code)]
        
        return dp(0, 0)