# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def findDepth(root):
            if not root:
                return 0
            left = findDepth(root.left)
            right = findDepth(root.right)
            return max(left, right) + 1
        res = 0
        queue = deque([root])
        while queue:
            cur = queue.popleft()
            res = max(res, findDepth(cur.left) + findDepth(cur.right))
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
        return res
        