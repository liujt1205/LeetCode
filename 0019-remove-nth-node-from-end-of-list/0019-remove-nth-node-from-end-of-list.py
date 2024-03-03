# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head
        remove = ListNode(-1, None)
        remove.next = head
        while cur.next:
            if n == 1:
                remove = remove.next
            else:
                n -= 1
            cur = cur.next
        if remove.next != head:
            remove.next = remove.next.next
        else:
            return head.next
        return head