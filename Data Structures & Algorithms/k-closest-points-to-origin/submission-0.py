class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for point in points:
            x1, y1 = point
            dist = math.sqrt((x1) ** 2 + y1 ** 2)
            heapq.heappush(heap, (-dist, point))

            if len(heap) > k:
                heapq.heappop(heap)
        
        return [point for dist, point in heap]