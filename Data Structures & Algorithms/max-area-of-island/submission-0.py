class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ## if allowed to edit grid, edit
        ## otherwise use more space for visited

        def dfs(i, j):
            if i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0]) and grid[i][j] == 1:
                grid[i][j] = 2

                return 1 + dfs(i + 1, j) + dfs(i - 1, j) + dfs(i, j + 1) + dfs(i, j - 1)
            return 0
        
        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    max_area = max(max_area, dfs(i, j))

        return max_area