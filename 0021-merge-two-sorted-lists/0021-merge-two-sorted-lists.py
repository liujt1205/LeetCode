# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(-1)
        pointer1 = list1
        pointer2 = list2
        cur = head
        while pointer1 and pointer2:
            if pointer1.val <= pointer2.val:
                cur.next = pointer1
                pointer1 = pointer1.next
            else:
                cur.next = pointer2
                pointer2 = pointer2.next
            cur = cur.next
                
        if pointer1:
            cur.next = pointer1
        if pointer2:
            cur.next = pointer2
            
        return head.next