class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = []
        m = Counter(tasks)

        for task in m:
            heapq.heappush(heap, (-m[task], task))

        cooldown = deque()
        time = 0

        while heap or cooldown:

            # Move tasks whose cooldown has expired back into heap
            while cooldown and cooldown[0][0] <= time:
                next_time, freq, task = cooldown.popleft()
                heapq.heappush(heap, (freq, task))

            if heap:
                freq, task = heapq.heappop(heap)

                # Execute task
                freq += 1  # frequencies are negative

                # If task remains, put it into cooldown
                if freq < 0:
                    cooldown.append((time + n + 1, freq, task))

            # Either execute a task or sit idle
            time += 1

        return time