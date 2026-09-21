class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ## path with the smallest max

        pq = [(grid[0][0], (0, 0), grid[0][0])]
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = set()

        while pq:
            val, coord, min_val = heapq.heappop(pq)
            x, y = coord

            if x == len(grid) - 1 and y == len(grid[0]) - 1:
                return min_val

            for d in dirs:
                new_x, new_y = x + d[0], y + d[1]

                if (new_x, new_y) not in visited and x + d[0] >= 0 and x + d[0] < len(grid) and y + d[1] >= 0 and y + d[1] < len(grid[0]):
                    new_x, new_y = x + d[0], y + d[1]
                    visited.add(coord)

                    heapq.heappush(pq, (grid[new_x][new_y], (new_x, new_y), max(min_val, grid[new_x][new_y])))
        
        return -1