# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        duplicate = {}
        cur = head
        while cur:
            if cur.val not in duplicate:
                duplicate[cur.val] = False
            else:
                duplicate[cur.val] = True
            cur = cur.next
        fhead = ListNode(0, head)
        pre = fhead
        cur = pre.next
        while cur:
            if not duplicate[cur.val]:
                pre.next = cur
                pre = cur
            cur = cur.next
        pre.next = None
        return fhead.next