# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        queue = deque([root])
        level = 0
        while queue:
            n = len(queue)
            odd = level % 2
            pre = 0 if not odd else 1000001
            for _ in range(n):
                cur = queue.popleft()
                if (cur.val % 2 == odd) or (cur.val >= pre if odd else cur.val <= pre):
                    return False
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
                pre = cur.val
            level += 1
        return True