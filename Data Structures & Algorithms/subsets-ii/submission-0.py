class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []

        def find_subset(i, temp):
            res.append(temp[::])

            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j - 1]:
                    continue
                
                temp.append(nums[j])
                find_subset(j + 1, temp)
                temp.pop()
        
        find_subset(0, [])
        
        return res