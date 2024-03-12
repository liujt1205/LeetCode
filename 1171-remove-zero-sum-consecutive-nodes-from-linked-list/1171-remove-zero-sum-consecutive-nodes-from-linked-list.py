# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sums = {}
        curSum = 0
        res = ListNode(-1)
        res.next = head
        sums[0] = res
        cur = res
        while cur:
            curSum += cur.val
            sums[curSum] = cur
            cur = cur.next
        curSum = 0
        cur = res
        while cur:
            curSum += cur.val
            cur.next = sums[curSum].next
            cur = cur.next
        return res.next