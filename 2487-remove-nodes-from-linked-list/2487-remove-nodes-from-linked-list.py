# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        cur = head
        while cur:
            while stack and stack[-1].val < cur.val:
                stack.pop()
            stack.append(cur)
            cur = cur.next
        newHead = stack[0]
        for i in range(len(stack)):
            if i < len(stack) - 1:
                stack[i].next = stack[i + 1]
            else:
                stack[i].next = None
        return newHead
            