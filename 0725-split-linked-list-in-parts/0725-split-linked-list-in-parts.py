# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next
            
        target = length // k
        reminder = length % k
        res = [[None] for _ in range(k)]
        cur = head
        prev = cur
        for i in range(k):
            newHead = cur
            count = target
            if reminder > 0:
                count += 1
                reminder -= 1
            for j in range(count):
                prev = cur
                if cur is not None:
                    cur = cur.next
            if prev is not None:
                prev.next = None
            res[i] = newHead    
            
        return res
            