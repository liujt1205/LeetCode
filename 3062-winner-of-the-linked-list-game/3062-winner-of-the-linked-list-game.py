# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def gameResult(self, head: Optional[ListNode]) -> str:
        cur = head
        score = 0
        while cur:
            even = cur
            odd = cur.next
            if even.val > odd.val:
                score += 1
            else:
                score -= 1
            cur = odd.next
        if score > 0:
            return "Even"
        elif score < 0:
            return "Odd"
        else:
            return "Tie"