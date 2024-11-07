# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        # find size of linked-list
        cur = head
        size = 0
        while cur:
            cur = cur.next
            size += 1
            
        def convert(left_index, right_index):
            nonlocal head
            if left_index > right_index:
                return None
            mid = (left_index + right_index) // 2
            left = convert(left_index, mid - 1)
            node = TreeNode(head.val)
            node.left = left
            head = head.next
            node.right = convert(mid + 1, right_index)
            return node
        
        return convert(0, size - 1)