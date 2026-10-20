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

        low, high = 0, len(self.probs) - 1

        while low < high:
            mid = (low + high) // 2

            if prob < self.probs[mid]:
                high = mid
            else:
                low = mid + 1
        
        return low


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()