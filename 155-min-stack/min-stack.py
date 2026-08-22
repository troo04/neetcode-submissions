
class MinStack:
    def __init__(self):
        self.stack = []
        self.min = float('inf')

    def push(self, val: int) -> None:
        if len(self.stack) == 0 or val < self.min:
            self.min = val
        self.stack.append((val, self.min))

    def pop(self) -> None:
        res = self.stack.pop()[0]
        if len(self.stack) != 0:
            self.min = self.stack[-1][1]

    def top(self) -> int:
        res = self.stack[-1][0]
        return res

    def getMin(self) -> int:
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()