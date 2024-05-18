# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        res = 0
        def balanceNode(node):
            if node is None:
                return 0
            nonlocal res
            left = balanceNode(node.left)
            right = balanceNode(node.right)
            res += abs(left) + abs(right)
            return node.val + left + right - 1
        
        balanceNode(root)
        return res