# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = head
        cur = head.next
        def findGCD(x, y):
            if x > y:
                return findGCD(y, x)
            if x == 0:
                return y
            y %= x
            return findGCD(y, x)
        
        while cur:
            newNode = ListNode(findGCD(prev.val, cur.val))
            prev.next = newNode
            newNode.next = cur
            prev = cur
            cur = cur.next
            
        return head