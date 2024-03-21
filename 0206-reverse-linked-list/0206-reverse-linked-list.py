# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        curNode = None
        nextNode = head
        while nextNode:
            temp = nextNode
            nextNode = nextNode.next
            temp.next = curNode
            curNode = temp
            
        return curNode