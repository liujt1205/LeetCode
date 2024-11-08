# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def helper(node):
            if not node:
                return -float('inf'), -float('inf')
            
            bestLeft, lineLeft = helper(node.left)
            bestRight, lineRight = helper(node.right)
            
            curBest = max((max(0, lineLeft) + node.val + max(0, lineRight)), bestLeft, bestRight)
            lineBest = max((max(lineLeft, 0) + node.val), (max(lineRight, 0) + node.val))
            return curBest, lineBest
                           
        res, _ = helper(root)
        return res