# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(-1)
        cur = head
        carry = 0
        while l1 or l2:
            if not l1:
                num1 = 0
            else:
                num1 = l1.val
            if not l2:
                num2 = 0
            else:
                num2 = l2.val
            add = num1 + num2 + carry
            if add > 9:
                carry = 1
            else:
                carry = 0
            newNode = ListNode(add % 10)
            cur.next = newNode
            cur = cur.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        if carry:
            cur.next = ListNode(1)
            
        return head.next