# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max_dis = 0
    
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        self.traverse(root, start)
        return self.max_dis
        
    def traverse(self, root, start):
        depth = 0
        if root is None:
            return depth
        left_depth = self.traverse(root.left, start)
        right_depth = self.traverse(root.right, start)
        if root.val == start:
            self.max_dis = max(left_depth, right_depth)
            depth = -1
        elif left_depth >= 0 and right_depth >= 0:
            depth = max(left_depth, right_depth) + 1
        else:
            distance = abs(left_depth) + abs(right_depth)
            self.max_dis = max(self.max_dis, distance)
            depth = min(left_depth, right_depth) - 1
        return depth