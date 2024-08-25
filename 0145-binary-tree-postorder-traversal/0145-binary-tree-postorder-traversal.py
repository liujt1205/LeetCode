# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def helper(node, res):
            if not node:
                return
            helper(node.left, res)
            helper(node.right, res)
            res.append(node.val)
            
        res = []
        helper(root, res)
        return res