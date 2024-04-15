# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        queue = deque()
        queue.append((root, False))
        while queue:
            cur, lonely = queue.popleft()
            if lonely:
                res.append(cur.val)
            if cur.left and not cur.right:
                queue.append((cur.left, True))
            if cur.right and not cur.left:
                queue.append((cur.right, True))
            if cur.right and cur.left:
                queue.append((cur.left, False))
                queue.append((cur.right, False))
        return res