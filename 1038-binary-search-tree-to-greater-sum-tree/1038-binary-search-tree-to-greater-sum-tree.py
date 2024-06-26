# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def helper(node, sumFromAbove):
            if node.right:
                larger = helper(node.right, sumFromAbove)
            else:
                larger = sumFromAbove
            node.val = node.val + larger
            if node.left:
                return helper(node.left, node.val)
            else:
                return node.val
            
        helper(root, 0)
        return root