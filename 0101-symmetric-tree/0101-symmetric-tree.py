# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        left = deque()
        right = deque()
        left.append(root)
        right.append(root)
        while left:
            left_node = left.pop()
            right_node = right.pop()
            if left_node.val != right_node.val:
                return False

            if left_node.right and right_node.left:
                left.append(left_node.right)
                right.append(right_node.left)
            elif left_node.right or right_node.left:
                return False

            if left_node.left and right_node.right:
                left.append(left_node.left)
                right.append(right_node.right)
            elif left_node.left or right_node.right:
                return False

        return not right
            