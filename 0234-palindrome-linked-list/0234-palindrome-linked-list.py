# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        values = []
        node = head
        while node:
            values.append(node.val)
            node = node.next
        
        left = 0
        right = len(values) - 1
        while left < right:
            if values[left] != values[right]:
                return False
            left += 1
            right -= 1
        return True