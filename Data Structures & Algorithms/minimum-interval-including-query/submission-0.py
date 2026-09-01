class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        min_heap = []
        res = {}
        i = 0

        for q in sorted(queries):
            while i < len(intervals) and q >= intervals[i][0]:
                l, r = intervals[i]
                heapq.heappush(min_heap, (r - l + 1, r))
                i += 1
            
            while min_heap and min_heap[0][1] < q:
                heapq.heappop(min_heap)
            
            if min_heap:
                res[q] = min_heap[0][0]
            else:
                res[q] = -1
        
        return [res[q] for q in queries]