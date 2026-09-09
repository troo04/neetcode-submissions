# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0

        dummy = ListNode()
        head = dummy

        while l1 and l2:
            res = (l1.val + l2.val + carry) % 10
            carry = (l1.val + l2.val + carry) // 10

            dummy.next = ListNode(res)
            dummy = dummy.next
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            res = (l1.val + carry) % 10
            carry = (l1.val + carry) // 10

            dummy.next = ListNode(res)
            dummy = dummy.next
            l1 = l1.next
        
        while l2:
            res = (l2.val + carry) % 10
            carry = (l2.val + carry) // 10

            dummy.next = ListNode(res)
            dummy = dummy.next
            l2 = l2.next
        
        if carry > 0:
            dummy.next = ListNode(carry)
            dummy = dummy.next
        
        return head.next