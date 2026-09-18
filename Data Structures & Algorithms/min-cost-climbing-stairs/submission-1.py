class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = {}
        def find_min_cost(i):
            if i in cache:
                return cache[i]
            
            if i > len(cost):
                return 101

            if i == len(cost):
                return 0


            cache[i] = min(cost[i] + find_min_cost(i + 1), cost[i] + find_min_cost(i + 2))

            return cache[i]
        
        return min(find_min_cost(0), find_min_cost(1))