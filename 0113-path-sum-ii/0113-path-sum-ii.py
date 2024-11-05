# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        if not root:
            return []
        
        def helper(node, curSum, path):
            curSum += node.val
            path.append(node.val)
            isLeaf = True
            if node.left:
                helper(node.left, curSum, path)
                isLeaf = False
            if node.right:
                helper(node.right, curSum, path)
                isLeaf = False
            if isLeaf and curSum == targetSum:
                res.append(path[:])
            path.pop()
                
        helper(root, 0, [])
        return res