class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        ## in this case, since we are doing prims and the graph is quite dense with n nodes and n^2 edges, doing a linear pass to find the smallest next edge to proceed with is cheaper than maintaining the relative order of n^2 edges with a pq

        n = len(points)

        start = (points[0][0], points[0][1])
            
        min_dist = [float("inf")] * n
        min_dist[0] = 0

        visited = set()
        path_sum = 0

        while len(visited) < n:
            min_edge, min_node = float('inf'), -1

            for i, dist in enumerate(min_dist):
                if i not in visited and dist < min_edge:
                    min_edge = dist
                    min_node = i

            visited.add(min_node)
            path_sum += min_edge

            for i, node in enumerate(points):
                x, y = node

                if i in visited:
                    continue
                
                x_o, y_o = points[min_node]
                
                min_dist[i] = min(min_dist[i], abs(x_o - x) + abs(y_o - y))
        
        return path_sum
