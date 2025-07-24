# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head


        fakeHead = ListNode(-200)
        prev = fakeHead
        cur = head
        while cur:
            if not cur.next or cur.next.val != cur.val:
                prev.next = cur
                prev = prev.next
            else:
                while cur.next and cur.val == cur.next.val:
                    cur = cur.next
            cur = cur.next

        prev.next = None

        return fakeHead.next