class Solution:
    def trap(self, height: List[int]) -> int:
        pre_max = [0] * len(height)
        pre_max[0] = height[0]
        suf_max = [0] * len(height)
        suf_max[-1] = height[-1]

        for i in range(1, len(height)):
            pre_max[i] = max(pre_max[i - 1], height[i])
        
        for i in range(len(height) - 2, -1, -1):
            suf_max[i] = max(suf_max[i + 1], height[i])

        area = 0
        for i in range(len(height)):
            area += min(pre_max[i], suf_max[i]) - height[i]

        return area