class Solution:
    def jump(self, nums: List[int]) -> int:
        start, end = 0, 0
        jumps = 0

        while end < len(nums) - 1:
            temp = end
            for i in range(start, end + 1):
                end = max(end, i + nums[i])
            start = temp + 1
            jumps += 1
        
        return jumps