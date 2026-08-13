class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        semesters = 0
        indegree = [0 for _ in range(n + 1)]
        adj_map = {i + 1: [] for i in range(n)}

        for relation in relations:
            indegree[relation[1]] += 1
            adj_map[relation[0]].append(relation[1])
        
        queue = deque([i for i in range(1, n + 1) if indegree[i] == 0])
        visited = 0

        while queue:
            semesters += 1
            nodes = len(queue)

            for _ in range(nodes):
                node = queue.popleft()
                visited += 1

                for neigh in adj_map[node]:
                    indegree[neigh] -= 1
                    if indegree[neigh] == 0:
                        queue.append(neigh)
        
        if visited != n:
            return -1
        
        return semesters