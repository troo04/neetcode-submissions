class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        queue = deque()

        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    queue.append((i, j, 0))

        visited = set()

        while queue:
            level = len(queue)

            for _ in range(level):
                node = queue.popleft()

                if node[0] < 0 or node[0] >= len(rooms) or node[1] < 0 or node[1] >= len(rooms[0]):
                    continue

                if (node[0], node[1]) in visited or rooms[node[0]][node[1]] == -1:
                    continue
                
                rooms[node[0]][node[1]] = node[2]
                visited.add((node[0], node[1]))
                
                for d in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                    dx, dy = d

                    queue.append((node[0] + dx, node[1] + dy, node[2] + 1))