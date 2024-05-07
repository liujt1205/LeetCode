# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def helper(node):
            if not node:
                return 0
            new = node.val * 2 + helper(node.next)
            node.val = new % 10
            return new // 10
        
        carry = helper(head)
        if carry:
            head = ListNode(carry, head)
        return head