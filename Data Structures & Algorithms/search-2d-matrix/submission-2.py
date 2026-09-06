class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ## 0 1 2 3
        ## 4 5 6 7
        ## 8 9 10 11
        low, high = 0, len(matrix)*len(matrix[0]) - 1

        while low <= high:
            mid = (low + high) // 2

            if matrix[mid // len(matrix[0])][mid % len(matrix[0])] == target:
                return True
            elif matrix[mid // len(matrix[0])][mid % len(matrix[0])] > target:
                high = mid - 1
            else:
                low = mid + 1
        
        return False