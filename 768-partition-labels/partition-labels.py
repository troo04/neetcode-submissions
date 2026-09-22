class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ## x: 1,4 y: 2,5 z: 6,8 b: 7,10 i: 11,11 s: 12,12 l: 13,13

        ## get the start
        # mappings = defaultdict(list)

        # for i, letter in enumerate(s):
        #     if mappings[letter] == []:
        #         mappings[letter].append(i)
        
        # ## get the end
        # for i, letter in enumerate(reversed(s)):
        #     if len(mappings[letter]) == 1:
        #         mappings[letter].append(len(s) - i - 1)
        
        # ## merge the intervals
        # intervals = list(mappings.values())
        # res = []
        
        # intervals.sort()
        # prev = intervals[0]
        
        # for i in range(1, len(intervals)):
        #     if intervals[i][0] <= prev[1]:
        #         prev[1] = max(prev[1], intervals[i][1])
        #     else:
        #         res.append(prev)
        #         prev = intervals[i]
        # res.append(prev)
        
        # return [j - i + 1 for i, j in res]

        lastIndex = {}
        for i, c in enumerate(s):
            lastIndex[c] = i
        
        res = []
        size = 0
        end = 0

        for i, c in enumerate(s):
            size += 1
            end = max(end, lastIndex[c])

            if i == end:
                res.append(size)
                size = 0
        
        return res