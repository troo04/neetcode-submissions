class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = [nums[0]]

        for i in range(1, len(nums)):
            if nums[i] > res[-1]:
                res.append(nums[i])
            else:
                low, high = 0, len(res)
                mid = low + ((high - low) / 2)

                while low < high:
                    mid = low + ((high - low) // 2)

                    if res[mid] < nums[i]:
                        low = mid + 1
                    else:
                        high = mid
                
                res[low] = nums[i]

        return len(res)