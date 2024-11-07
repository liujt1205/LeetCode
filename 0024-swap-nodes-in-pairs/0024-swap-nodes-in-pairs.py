# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fakeHead = ListNode(-1)
        fakeHead.next = head
        curNode = fakeHead
        while head and head.next:
            first = head
            second = head.next
            
            head = second.next
            curNode.next = second
            second.next = first
            first.next = head
            curNode = first
            
        return fakeHead.next