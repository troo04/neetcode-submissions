class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    queue.append((i, j, 0))

        visited = set()

        while queue:
            level = len(queue)

            for _ in range(level):
                node = queue.popleft()

                if node[0] < 0 or node[0] >= len(grid) or node[1] < 0 or node[1] >= len(grid[0]):
                    continue

                if (node[0], node[1]) in visited or grid[node[0]][node[1]] == -1:
                    continue
                
                grid[node[0]][node[1]] = node[2]
                visited.add((node[0], node[1]))
                
                for d in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                    dx, dy = d

                    queue.append((node[0] + dx, node[1] + dy, node[2] + 1))