# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        res = 0
        queue = deque()
        queue.append((root, 0))
        while queue:
            cur, val = queue.popleft()
            if cur.left:
                queue.append((cur.left, cur.left.val))
            if cur.right:
                queue.append((cur.right, 0))
            if not cur.left and not cur.right:
                res += val
        return res