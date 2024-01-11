# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        if not root:
            return self.res
        def helper(node, curMax, curMin):
            if not node:
                return
            self.res = max(self.res, abs(curMax - node.val), abs(curMin - node.val))
            curMax = max(curMax, node.val)
            curMin = min(curMin, node.val)
            helper(node.left, curMax, curMin)
            helper(node.right, curMax, curMin)
        helper(root, root.val, root.val)
        return self.res