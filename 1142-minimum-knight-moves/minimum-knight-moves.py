class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        ## bfs traversal

        ## create moves array, size 8
        moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, 2), (1, -2), (2, -1), (2, 1)]
        ## create queue, visited
        queue = deque([(0, 0)])
        visited = set()
        steps = 0

        while queue:
            ## iterate through each level
            count = len(queue)

            for _ in range(count):
                pos = queue.popleft()
                ## check if that pos is the end position
                if pos == (x, y):
                    return steps
                ## loop through the moves array and add the new coords to the queue, as long as they are not visited
                for move in moves:
                    new_x, new_y = pos[0] + move[0], pos[1] + move[1]

                    if (new_x, new_y) not in visited:
                        queue.append((new_x, new_y))
                        visited.add((new_x, new_y))

            steps += 1

        return steps 
