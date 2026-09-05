class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj_map = defaultdict(list)
        
        for flight in flights:
            s, dest, cost = flight
            adj_map[s].append((dest, cost))
        
        prices = [float('inf')] * n
        prices[src] = 0

        queue = deque([(0, src, 0)])
        while queue:
            node = queue.popleft()
            
            if node[2] > k:
                continue
            
            for nei, c in adj_map[node[1]]:
                if c + node[0] < prices[nei]:
                    prices[nei] = c + node[0]
                    queue.append((prices[nei], nei, node[2] + 1))
        
        if prices[dst] == float('inf'):
            return -1
        else:
            return prices[dst]