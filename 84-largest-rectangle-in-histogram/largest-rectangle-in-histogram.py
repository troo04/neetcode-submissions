class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights = [0] + heights + [0]
        stack = []
        largest = 0

        for i in range(len(heights)):
            while stack and heights[stack[-1]] >= heights[i]:
                height = heights[stack.pop()]
                width = i - stack[-1] - 1 if stack else i
                largest = max(largest, height * width)

            stack.append(i)
        
        return largest