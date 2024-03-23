# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        res = None
        cur = slow
        while cur:
            temp = cur.next
            cur.next = res
            res = cur
            cur = temp    
            
        first = head
        second = res
        
        while second.next:
            tempNext = first.next
            tempEnd = second.next
            first.next = second
            second.next = tempNext
            first = tempNext
            second = tempEnd
