class Solution:
    def countPairs(self, deliciousness: list[int]) -> int:
        targets = set([2 ** i for i in range(0, 22)])

        seen = defaultdict(int)

        res = 0

        for d in deliciousness:
            for target in targets:
                if target - d in seen:
                    res += seen[target - d]
            
            seen[d] += 1
        
        return res % (10 ** 9 + 7)