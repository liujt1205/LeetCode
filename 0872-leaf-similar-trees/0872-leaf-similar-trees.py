# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        sq1 = deque()
        sq2 = deque()
        def dfs(root: Optional[TreeNode], storage: deque):
            if root is None:
                return
            if root.left is None and root.right is None:
                storage.append(root.val)
            else:
                dfs(root.left, storage)
                dfs(root.right, storage)
        dfs(root1, sq1)
        dfs(root2, sq2)
        return sq1 == sq2
                
            