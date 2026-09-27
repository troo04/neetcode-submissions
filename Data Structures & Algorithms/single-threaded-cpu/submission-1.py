class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        ## priority queue (time, processing_time, index)
        pq = []

        res = []

        for i, t in enumerate(tasks):
            enq, proc = t
            heapq.heappush(pq, (enq, proc, i))

        ## start with time at min of priority queue
        time = pq[0][0]
        new_pq = []
        ## while priority queue
        while pq or new_pq:
            ## while queue[0] <= time
            while pq and pq[0][0] <= time:
                _, old_p, old_i = heapq.heappop(pq)
                heapq.heappush(new_pq, (old_p, old_i))
                ## pop, and to new priority queue with just processing time and index
            if not new_pq:
                time = pq[0][0]
                continue

            ## pop, add to res, add to overall time
            p, i = heapq.heappop(new_pq)
            res.append(i)
            time += p
        
        return res