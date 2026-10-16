class Solution:
    def shortestDistance(self, wordsDict: list[str], word1: str, word2: str) -> int:
        
        i1 = -1
        i2 = -1

        min_dst = float('inf')

        for i in range(len(wordsDict)):
            if wordsDict[i] == word1:
                i1 = i
            elif wordsDict[i] == word2:
                i2 = i
            
            if i1 != -1 and i2 != -1:
                min_dst = min(min_dst, abs(i1 - i2))
        
        return min_dst