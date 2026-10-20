class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_ele = -1
        res = [0] * len(arr)

        for i in range(len(arr) - 1, -1, -1):
            res[i] = max_ele
            max_ele = max(max_ele, arr[i])
        
        return res