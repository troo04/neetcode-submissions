class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj_map = defaultdict(list)
        
        for flight in flights:
            s, dest, cost = flight
            adj_map[s].append((dest, cost))
        
        best = {}

        queue = [(0, src, 0)]
        while queue:
            node = heapq.heappop(queue) 
            
            if (node[1], node[2]) in best and best[(node[1], node[2])] <= node[0]:
                continue

            best[(node[1], node[2])] = node[0]

            if node[1] == dst:
                return node[0]
            
            if node[2] > k:
                continue

            for neighbor in adj_map[node[1]]:
                new_state = (neighbor[0], node[2] + 1)
                new_cost = node[0] + neighbor[1]

                if new_state not in best or new_cost < best[new_state]:
                    heapq.heappush(queue, (new_cost, neighbor[0], node[2] + 1))
        
        return -1