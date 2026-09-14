class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        start = (points[0][0], points[0][1])
            
        pq = [(0, start)]
        visited = set()
        path_sum = 0

        while pq and len(visited) < n:
            cost, node = heapq.heappop(pq)
            x, y = node

            if node in visited:
                continue

            visited.add(node)
            path_sum += cost

            for x_o, y_o in points:
                if x == x_o and y == y_o:
                    continue
                
                if (x_o, y_o) in visited:
                    continue
                
                heapq.heappush(pq, (abs(x_o - x) + abs(y_o - y), (x_o, y_o)))
        
        return path_sum
