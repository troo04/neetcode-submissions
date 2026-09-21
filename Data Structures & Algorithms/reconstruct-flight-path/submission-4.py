class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        visited = set()
        total = len(tickets)

        adj_map = {}

        for (f, t) in tickets:
            if f not in adj_map:
                adj_map[f] = []
            adj_map[f].append(t)
        
        for k in adj_map:
            adj_map[k].sort(reverse=True)
        
        res = []
        def dfs(node):
            if node in adj_map:
                while adj_map[node]:
                    neighbor = adj_map[node].pop()
                    dfs(neighbor)
            res.append(node)
        
        dfs("JFK")
        return res[::-1]