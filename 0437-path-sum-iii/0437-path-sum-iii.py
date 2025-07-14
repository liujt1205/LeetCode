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
        def helper(node, preSum):
            if not node:
                return
            curSum = preSum + node.val
            if curSum == targetSum:
                res[0] += 1
            
            res[0] += count[curSum - targetSum]
            count[curSum] += 1
            helper(node.left, curSum)
            helper(node.right, curSum)
            count[curSum] -= 1

        count = defaultdict(int)
        helper(root, 0)
        return res[0]
            