class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        r = len(nums) - 1

        i = 0
        while i <= r:
            if nums[i] == 0:
                ## since we processed everyhting to the left its safe to say we dont need to do the check again for this i
                nums[l], nums[i] = nums[i], nums[l]
                l += 1
                i += 1
            elif nums[i] == 2:
                ## same CANNOT be said for 2
                nums[r], nums[i] = nums[i], nums[r]
                r -= 1
            else:
                i += 1