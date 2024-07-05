# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        firstC, preC, preV = -1, -1, head.val
        smallest = float('inf')
        cur = head
        while cur.next is not None:
            if (cur.val < preV and cur.val < cur.next.val) or (cur.val > preV and cur.val > cur.next.val):
                if firstC == -1:
                    firstC = 0
                else:
                    smallest = min(smallest, preC)
                preC = 0
            if firstC != -1:
                firstC += 1
                preC += 1
            preV = cur.val
            cur = cur.next
        if firstC == preC:
            return [-1, -1]
        else:
            return [smallest, firstC - preC]