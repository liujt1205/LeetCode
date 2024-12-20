# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(leftNode, rightNode, level):
            if not leftNode or not rightNode:
                return
            if level % 2 != 0:
                temp = leftNode.val
                leftNode.val = rightNode.val
                rightNode.val = temp
                
            dfs(leftNode.left, rightNode.right, level + 1)
            dfs(leftNode.right, rightNode.left, level + 1)
            
        dfs(root.left, root.right, 1)
        return root