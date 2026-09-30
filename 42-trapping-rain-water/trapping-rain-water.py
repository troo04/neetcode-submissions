class Solution:
    def trap(self, height: list[int]) -> int:
        l, r = 0, len(height) - 1

        left_max, right_max = height[l], height[r]
        res = 0

        while l < r:
            if left_max < right_max:
                l += 1
                res += max(0, left_max - height[l])
                left_max = max(left_max, height[l])
            else:
                r -= 1
                res += max(0, right_max - height[r])
                right_max = max(right_max, height[r])
        
        return res
