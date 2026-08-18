class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        ## dfs to find first island

        self.queue = deque()
        self.visited = set()

        dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        def dfs(i, j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
                return
            
            if (i, j) in self.visited or grid[i][j] == 0:
                return
            
            self.visited.add((i, j))
            grid[i][j] = 2
            self.queue.append(((i, j), 0))
            
            for d in dirs:
                dfs(i + d[0], j + d[1])
        
        found = False

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    dfs(i, j)
                    found = True
                    break
            if found:
                break
        
        ## do bfs from each cell from island 1

        while self.queue:
            num_neighbors = len(self.queue)

            for _ in range(num_neighbors):
                cell, dist = self.queue.popleft()
                i, j = cell

                for di, dj in dirs:
                    ni = i + di
                    nj = j + dj

                    if (ni < 0 or nj < 0 or ni >= len(grid) or nj >= len(grid[0])) or grid[ni][nj] == 2:
                        continue
                    
                    if grid[ni][nj] == 1:
                        return dist
                    
                    grid[ni][nj] = 2
                    self.queue.append(((ni, nj), dist + 1))
                
        return -1