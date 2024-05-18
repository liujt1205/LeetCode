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
            res += abs(balanceNode(node.left)) + abs(balanceNode(node.right))
            return node.val + balanceNode(node.left) + balanceNode(node.right) - 1
        
        balanceNode(root)
        return res