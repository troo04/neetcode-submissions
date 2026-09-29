# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        if not head:
            return None
        
        if k == 0:
            return head
        
        length = 1
        tail = head
        while tail and tail.next:
            tail = tail.next
            length += 1

        k %= length
        if k == 0:
            return head

        tail.next = head
        temp = head
        for _ in range(length - k - 1):
            temp = temp.next
        res = temp.next
        temp.next = None

        return res