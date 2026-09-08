class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)

        while low <= high:
            k = (low + high) // 2
            temp_hours = 0
            
            for pile in piles:
                temp_hours += math.ceil(pile / k)
            
            if temp_hours > h:
                low = k + 1
            else:
                high = k - 1
        
        return low