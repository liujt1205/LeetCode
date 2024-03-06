# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        fast = head.next
        slow = head
        while fast != None:
            if fast == slow:
                return True
            if fast.next:
                fast = fast.next.next
            else:
                return False
            slow = slow.next
        