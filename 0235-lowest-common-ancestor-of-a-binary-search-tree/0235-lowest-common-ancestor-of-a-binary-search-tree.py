# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        res = [None]
        def dfs(node):
            if not node:
                return False
            
            left = dfs(node.left)
            right = dfs(node.right)
            itself = node.val == p.val or node.val == q.val
            
            if left + right + itself >= 2:
                res[0] = node
                
            return left or right or itself
        
        dfs(root)
        return res[0]