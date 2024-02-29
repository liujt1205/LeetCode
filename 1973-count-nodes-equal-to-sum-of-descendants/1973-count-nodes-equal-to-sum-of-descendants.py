# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def equalToDescendants(self, root: Optional[TreeNode]) -> int:
        res = 0
        def getSum(node):
            nonlocal res
            leftSide = getSum(node.left) + node.left.val if node.left else 0
            rightSide = getSum(node.right) + node.right.val if node.right else 0
            if node.val == leftSide + rightSide:
                res += 1
            return leftSide + rightSide
        getSum(root)
        return res