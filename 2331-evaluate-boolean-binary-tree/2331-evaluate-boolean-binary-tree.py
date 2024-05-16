# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def check(node):
            if node.val <= 1:
                return node.val
            elif node.val == 2:
                return check(node.left) or check(node.right)
            else:
                return check(node.left) and check(node.right)
            
        return check(root)