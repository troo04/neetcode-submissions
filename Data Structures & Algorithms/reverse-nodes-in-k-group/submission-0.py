# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        group_prev = dummy
        prev, cur = None, head

        while True:
            kth = group_prev
            
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next

            group_next = kth.next

            prev, cur = group_next, group_prev.next
            for _ in range(k):
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
            
            temp = group_prev.next ## 4
            group_prev.next = kth ## 3.next = dummy
            group_prev = temp ## 4

        return dummy.next