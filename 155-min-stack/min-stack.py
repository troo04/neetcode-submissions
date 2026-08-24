class MinStack:

    def __init__(self):
        self.stack = []
        self.smallest = float('inf')

    def push(self, val: int) -> None:
        self.smallest = min(self.smallest, val)
        self.stack.append((val, self.smallest))

    def pop(self) -> None:
        if self.stack and self.stack.pop()[1] == self.smallest:
            if self.stack:
                self.smallest = self.stack[-1][1]
        
        if not self.stack:
            self.smallest = float('inf')

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.smallest
