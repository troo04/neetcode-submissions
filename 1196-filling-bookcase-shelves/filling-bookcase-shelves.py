class Solution:
    def minHeightShelves(self, books: list[list[int]], shelfWidth: int) -> int:
        cache = {}

        def dp(i, rem_width, height):
            if (i, rem_width, height) in cache:
                return cache[(i, rem_width, height)]
            
            if i == len(books):
                return height
            
            w, h = books[i]

            cache[(i, rem_width, height)] = float('inf')
            if w <= rem_width:
                cache[(i, rem_width, height)] = dp(i + 1, rem_width - w, max(h, height))
            
            cache[(i, rem_width, height)] = min(cache[(i, rem_width, height)], height + dp(i + 1, shelfWidth - w, h))
        
            return cache[(i, rem_width, height)]
        
        return dp(0, shelfWidth, 0)