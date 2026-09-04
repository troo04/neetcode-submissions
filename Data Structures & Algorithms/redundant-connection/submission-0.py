class DSU:
    def find(self, parent, i):
        if i == parent[i]:
            return i
        return self.find(parent, parent[i])
    
    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1
    
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = DSU()
        parent, rank = [], []

        for node in range(len(edges) + 1):
            parent.append(node)
            rank.append(0)
        
        i = 0
        while i < len(edges):
            u, v = edges[i]

            x = dsu.find(parent, u)
            y = dsu.find(parent, v)
            if x != y:
                dsu.union(parent, rank, x, y)
            else:
                return edges[i]

            i += 1