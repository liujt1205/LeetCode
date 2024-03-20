# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        start = list1
        end = list1
        for i in range(b):
            if i == a - 1:
                start = end
            end = end.next
        
        start.next = list2
        cur = list2
        while cur.next is not None:
            cur = cur.next
        cur.next = end.next
        return list1