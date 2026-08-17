class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts = [0] + sorted(cuts) + [n]
        memo = {}

        def find_cost(left, right):
            if right - left == 1:
                return 0
            
            if (left, right) in memo:
                return memo[(left, right)]
            
            ans = float('inf')

            for mid in range(left + 1, right):
                ans = min(ans, find_cost(left, mid) + find_cost(mid, right) + cuts[right] - cuts[left])

            memo[(left, right)] = ans
            return ans
        
        return find_cost(0, len(cuts) - 1)
        