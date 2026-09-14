class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        start = (points[0][0], points[0][1])

        adj_map = {}

        for x, y in points:
            if (x, y) not in points:
                adj_map[(x, y)] = []
            
            for x_o, y_o in points:
                if x == x_o and y == y_o:
                    continue
                
                adj_map[(x, y)].append((x_o, y_o, abs(x_o - x) + abs(y_o - y)))
            
        pq = [(0, start)]
        visited = set()
        path_sum = 0

        while pq and len(visited) < n:
            cost, node = heapq.heappop(pq)

            if node in visited:
                continue

            visited.add(node)
            path_sum += cost

            for neighbor in adj_map[node]:
                if neighbor not in visited:
                    heapq.heappush(pq, (neighbor[2], (neighbor[0], neighbor[1])))
        
        return path_sum
