# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def helper(pre_start, pre_end, post_start, preorder, index_map):
            if pre_start > pre_end:
                return None
            root = TreeNode(preorder[pre_start])
            if pre_start == pre_end:
                return root
            leftRoot = preorder[pre_start + 1]
            leftCount = index_map[leftRoot] - post_start + 1

            root.left = helper(pre_start + 1, pre_start + leftCount, post_start, preorder, index_map)
            root.right = helper(pre_start + leftCount + 1, pre_end, post_start + leftCount, preorder, index_map)
            
            return root

        index_map = [0] * (len(preorder) + 1)
        for i in range(len(preorder)):
            index_map[postorder[i]] = i

        return helper(0, len(preorder) - 1, 0, preorder, index_map)