# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        memo = defaultdict(list)
        def helper(node, row, col):
            if not node:
                return
            memo[col].append((row, node.val))
            helper(node.left, row + 1, col - 1)
            helper(node.right, row + 1, col + 1)
            
        helper(root, 0, 0)
        res = []
        for col in sorted(memo.keys()):
            res.append([val for row, val in sorted(memo[col])])
            
        return res