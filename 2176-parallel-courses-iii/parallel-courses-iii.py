class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        indegree = [0] * (n + 1)
        adj_map = {i : [] for i in range(1, n + 1)}

        for r in relations:
            indegree[r[1]] += 1
            adj_map[r[0]].append(r[1])
        

        queue = deque([i for i in range(1, n + 1) if indegree[i] == 0])
        maxTime = [0] * (n + 1)

        while queue:
            node = queue.popleft()
            
            maxTime[node] = max(maxTime[node], time[node - 1])

            for neigh in adj_map[node]:
                maxTime[neigh] = max(maxTime[neigh], maxTime[node] + time[neigh - 1])
                indegree[neigh] -= 1

                if indegree[neigh] == 0:
                    queue.append(neigh)
            
        
        return max(maxTime)