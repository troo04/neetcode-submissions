class RLEIterator:

    def __init__(self, encoding: list[int]):
        self.encoding = encoding
        self.pointer = 0

    def next(self, n: int) -> int:
        used = 0

        while self.pointer < len(self.encoding):            
            will_use = min(self.encoding[self.pointer], n - used)
            
            used += will_use
            self.encoding[self.pointer] -= will_use

            if used == n:
                return self.encoding[self.pointer + 1]

            if self.encoding[self.pointer] == 0:
                self.pointer += 2
        
        return -1


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)