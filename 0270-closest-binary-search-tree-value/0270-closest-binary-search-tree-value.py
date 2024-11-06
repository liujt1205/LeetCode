# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        res = float('inf')
        cur = root
        while cur:
            if abs(cur.val - target) < abs(res - target) or (cur.val < res and abs(cur.val - target) == abs(res - target)):
                res = cur.val
                
            if cur.val < target:
                cur = cur.right
            else:
                cur = cur.left
                
        return res