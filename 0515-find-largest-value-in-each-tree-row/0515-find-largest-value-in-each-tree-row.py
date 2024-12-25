# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        queue = deque()
        res = []
        queue.append(root)
        while queue:
            largest = -float('inf')
            for _ in range(len(queue)):
                cur = queue.popleft()
                largest = max(largest, cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            res.append(largest)
            
        return res