class StockSpanner:

    def __init__(self):
        self.prices = []
        self.stack = []

    def next(self, price: int) -> int:
        ## 100 80 60 70 60 75
        ## 0   1  5

        cur_index = len(self.prices)
        
        while self.stack and price >= self.prices[self.stack[-1]]:
            self.stack.pop()
        
        prev_index = self.stack[-1] if self.stack else -1
        res = cur_index - prev_index
        self.stack.append(cur_index)
        self.prices.append(price)

        return res


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)