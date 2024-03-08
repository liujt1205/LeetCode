# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def frequenciesOfElements(self, head: Optional[ListNode]) -> Optional[ListNode]:
        freqs = defaultdict(int)
        cur = head
        while cur:
            freqs[cur.val] += 1
            cur = cur.next
        res = None
        for i in freqs.values():
            newHead = ListNode(i, res)
            res = newHead
        return res