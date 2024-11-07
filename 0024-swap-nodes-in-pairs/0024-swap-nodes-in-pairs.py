# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def helper(node):
            if not node or not node.next:
                return node
            newHead = node.next
            node.next = helper(newHead.next)
            newHead.next = node
            return newHead
        
        return helper(head)