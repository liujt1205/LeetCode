# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        mid = self.getMid(head)
        left = self.sortList(head)
        right = self.sortList(mid)
        return self.merge(left, right)

    def getMid(self, node):
        slow = ListNode()
        slow.next = node
        while node and node.next:
            node = node.next.next
            slow = slow.next
        mid = slow.next
        slow.next = None
        return mid

    def merge(self, left, right):
        fakeHead = ListNode()
        cur = fakeHead
        while left and right:
            if left.val < right.val:
                cur.next = left
                left = left.next
            else:
                cur.next = right
                right = right.next
            cur = cur.next
        if left:
            cur.next = left
        else:
            cur.next = right

        return fakeHead.next
            