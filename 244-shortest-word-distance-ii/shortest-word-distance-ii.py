class WordDistance:

    def __init__(self, wordsDict: list[str]):
        self.indices = defaultdict(list)

        for i, word in enumerate(wordsDict):
            self.indices[word].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        res = float('inf')

        arr1 = self.indices[word1]
        arr2 = self.indices[word2]
        
        i, j = 0, 0

        while i < len(arr1) and j < len(arr2):
            dist = abs(arr1[i] - arr2[j])

            if dist < res:
                res = dist
            
            if arr1[i] < arr2[j]:
                i += 1
            else:
                j += 1
        
        return res


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)