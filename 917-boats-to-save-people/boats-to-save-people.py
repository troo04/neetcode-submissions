class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        ## 1 2 2 3

        people.sort()

        l, r = 0, len(people) - 1
        boats = 0

        while l <= r:
            if people[l] + people[r] <= limit:
                l += 1
                r -= 1
                boats += 1
            else:
                boats += 1
                r -= 1
        
        return boats
