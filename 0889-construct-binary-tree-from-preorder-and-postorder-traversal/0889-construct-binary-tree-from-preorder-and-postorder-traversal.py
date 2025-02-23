# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def helper(pre_start, pre_end, post_start, preorder, postorder):
            if pre_start > pre_end:
                return None
            root = TreeNode(preorder[pre_start])
            if pre_start == pre_end:
                return root
            leftRoot = preorder[pre_start + 1]
            leftCount = 1
            while postorder[post_start + leftCount - 1] != leftRoot:
                leftCount += 1

            root.left = helper(pre_start + 1, pre_start + leftCount, post_start, preorder, postorder)
            root.right = helper(pre_start + leftCount + 1, pre_end, post_start + leftCount, preorder, postorder)
            
            return root

        return helper(0, len(preorder) - 1, 0, preorder, postorder)