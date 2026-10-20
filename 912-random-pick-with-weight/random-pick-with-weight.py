import random

class Solution:

    def __init__(self, w: list[int]):
        s = sum(w)
        self.probs = [0] * len(w)
        self.probs[0] = w[0] / s

        for i in range(1, len(w)):
            self.probs[i] = self.probs[i - 1] + (w[i] / s)

    def pickIndex(self) -> int:
        prob = random.random()

        i = 0
        while i < len(self.probs) and self.probs[i] < prob:
            i += 1
        
        return i


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()