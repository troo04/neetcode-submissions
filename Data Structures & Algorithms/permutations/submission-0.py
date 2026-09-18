class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        s = set(nums)
        res = []

        def find_permutation(perm, rem):
            if len(perm) == len(nums):
                res.append(list(perm)[::])

            for n in rem:
                perm.append(n)
                find_permutation(perm, rem - {n})
                perm.pop()
        
        find_permutation([], s)
            
        return res