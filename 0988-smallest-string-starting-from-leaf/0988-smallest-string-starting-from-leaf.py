# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        res = None
        queue = deque()
        queue.append((root, ""))
        while queue:
            cur, prefix = queue.popleft()
            newPrefix = chr(ord('a') + cur.val) + prefix
            if not cur.left and not cur.right:
                if not res:
                    res = newPrefix
                else:
                    res = min(res, newPrefix)
            if cur.left:
                queue.append((cur.left, newPrefix))
            if cur.right:
                queue.append((cur.right, newPrefix))
        return res
        