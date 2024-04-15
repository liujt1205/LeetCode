# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = 0
        queue = deque()
        queue.append((root, ""))
        while queue:
            cur, pre = queue.popleft()
            newPre = pre + str(cur.val)
            if not cur.left and not cur.right:
                res += int(newPre)
            if cur.left:
                queue.append((cur.left, newPre))
            if cur.right:
                queue.append((cur.right, newPre))
        return res