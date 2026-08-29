class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        heap = []
        queue = deque()

        for task in freq:
            heapq.heappush(heap, (-freq[task], task))
        
        timestamp = 0
        while heap or queue:
            while queue and queue[0][2] <= timestamp:
                freq, task, _ = queue.popleft()
                heapq.heappush(heap, (freq, task))
            
            if heap:
                count, task = heapq.heappop(heap)
                count += 1
                if count != 0:
                    queue.append((count, task, timestamp + n + 1))
                timestamp += 1
            else:
                timestamp = queue[0][2]
        
        return timestamp