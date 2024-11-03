# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        queue = deque()
        queue.append(root)
        while queue:
            last = None
            for i in range(len(queue)):
                cur = queue.popleft()
                if cur:
                    last = cur
                    queue.append(cur.left)
                    queue.append(cur.right)
            if last:
                res.append(last.val)
                
        return res