class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
    
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.lru = Node(-1, -1)
        self.mru = Node(-1, -1)
        self.capacity = capacity
        self.length = 0

        self.lru.next = self.mru
        self.mru.prev = self.lru
    
    def add(self, new_node):
        mru = self.mru.prev
        mru.next = new_node
        new_node.next = self.mru
        self.mru.prev = new_node
        new_node.prev = mru
    
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        return node

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.add(self.cache[key])
            
            return self.cache[key].value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].value = value
            removed = self.remove(self.cache[key])
            self.add(removed)
        else:
            new_node = Node(key, value)
            self.add(new_node)
            self.cache[key] = new_node
            self.length += 1

            ## evict (if needed)
            
            if self.length > self.capacity:
                removed = self.remove(self.lru.next)
                del self.cache[removed.key]

                self.length -= 1

