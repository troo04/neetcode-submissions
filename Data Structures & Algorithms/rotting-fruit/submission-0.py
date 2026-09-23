class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        queue = deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i, j))
        
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        minutes = 0

        while queue:
            rotten_count = len(queue)

            for _ in range(rotten_count):
                i, j = queue.popleft()

                for d in dirs:
                    new_i, new_j = i + d[0], j + d[1]

                    if 0 <= new_i < len(grid) and 0 <= new_j < len(grid[0]) and grid[new_i][new_j] == 1:
                        grid[new_i][new_j] = 2
                        queue.append((new_i, new_j))

            if queue:
                minutes += 1
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        
        return minutes