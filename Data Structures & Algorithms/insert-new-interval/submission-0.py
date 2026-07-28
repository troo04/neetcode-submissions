class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        
        intervals.append(newInterval)
        intervals.sort()
        
        res = []
        start, end = intervals[0][0], intervals[0][1]

        for i in range(1, len(intervals)):
            if intervals[i][0] > end:
                res.append([start, end])
                start = intervals[i][0]
                end = max(end, intervals[i][1])
            else:
                end = max(end, intervals[i][1])
        
        res.append([start, end])
        return res