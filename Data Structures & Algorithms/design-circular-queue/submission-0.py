class Node:
    def __init__(self, val):
        self.val = val
        self.n = None

class MyCircularQueue:

    def __init__(self, k: int):
        self.head = Node(-1)
        self.count = 0
        self.capacity = k

    def enQueue(self, value: int) -> bool:
        if self.count == self.capacity:
            return False
        
        head = self.head
        while head and head.n:
            head = head.n
        
        head.n = Node(value)
        self.count += 1
        return True

    def deQueue(self) -> bool:
        if self.count == 0:
            return False
        
        self.head.n = self.head.n.n
        self.count -= 1
        return True

    def Front(self) -> int:
        if self.count == 0:
            return -1
        
        return self.head.n.val

    def Rear(self) -> int:
        if self.count == 0:
            return -1
        
        temp = self.head
        while temp and temp.n:
            temp = temp.n
        return temp.val

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.capacity


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()