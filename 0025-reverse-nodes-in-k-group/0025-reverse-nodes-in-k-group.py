# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(head, k):
            newHead = None
            cur = head
            while k:
                nextNode = cur.next
                cur.next = newHead
                newHead = cur
                cur = nextNode
                k -= 1
            return newHead
            
        cur = head
        newHead = None
        newTail = None
        while cur:
            count = 0
            cur = head
            while count < k and cur:
                count += 1
                cur = cur.next
            if count == k:
                reverseHead = reverse(head, k)
                if not newHead:
                    newHead = reverseHead
                if newTail:
                    newTail.next = reverseHead
                newTail = head
                head = cur
        if newTail:
            newTail.next = head
        return newHead if newHead else head
                