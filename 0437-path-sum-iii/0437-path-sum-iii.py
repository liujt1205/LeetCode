# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0

        res = [0]
        def helper(node):
            if not node:
                return {}
            
            left = helper(node.left)
            right = helper(node.right)
            count = defaultdict(int)
            for pos in left:
                count[pos + node.val] += left[pos]
                if pos + node.val == targetSum:
                    res[0] += left[pos]
            for pos in right:
                count[pos + node.val] += right[pos]
                if pos + node.val == targetSum:
                    res[0] += right[pos]
            count[node.val] += 1
            if node.val == targetSum:
                res[0] += 1

            return count

        helper(root)
        return res[0]
            