class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist = [float('inf')] * (n + 1)

        dist[k] = 0
        adj_map = defaultdict(list)

        for src, target, time in times:
            adj_map[src].append((target, time))
        
        priority_queue = [(0, k)]
        
        while priority_queue:
            cur_dist, cur_node = heapq.heappop(priority_queue)

            if cur_dist > dist[cur_node]:
                continue
            
            for neigh, neigh_time in adj_map[cur_node]:
                if neigh_time + cur_dist < dist[neigh]:
                    heapq.heappush(priority_queue, (cur_dist + neigh_time, neigh))
                    dist[neigh] = cur_dist + neigh_time
        
        res = max([dist[i] for i in range(1, len(dist))])
        return res if res != float('inf') else -1