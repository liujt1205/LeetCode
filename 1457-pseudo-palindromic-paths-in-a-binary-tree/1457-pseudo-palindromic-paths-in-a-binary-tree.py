# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        res = [0]
        freq = [0] * 10
        def dfs(curNode, freq):
            freq[curNode.val] += 1
            if curNode.left is None and curNode.right is None:
                odd = 0
                for i in range(1, 10):
                    if freq[i] % 2 != 0:
                        odd += 1
                    if odd > 1:
                        break
                if odd <= 1:
                    res[0] += 1
            else:
                if curNode.left is not None:
                    dfs(curNode.left, freq)
                if curNode.right is not None:
                    dfs(curNode.right, freq)
            freq[curNode.val] -= 1
        dfs(root, freq)
        return res[0]