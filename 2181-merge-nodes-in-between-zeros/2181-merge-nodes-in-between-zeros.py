# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curSum = 0
        cur = head.next
        newNode = head
        while cur:
            if cur.val == 0:
                node = ListNode(curSum)
                newNode.next = node
                newNode = node
                curSum = 0
            else:
                curSum += cur.val
            cur = cur.next
        return head.next