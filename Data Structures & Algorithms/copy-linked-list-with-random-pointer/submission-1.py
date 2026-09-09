"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy = Node(0)

        m = {}
        res = dummy
        temp = head
        while temp:
            m[temp] = Node(temp.val)
            res.next = m[temp]
            res = res.next
            temp = temp.next
        
        temp = head
        res = dummy.next

        while temp:
            if temp.random:
                res.random = m[temp.random]
            else:
                res.random = None
            
            res = res.next
            temp = temp.next
        
        return dummy.next