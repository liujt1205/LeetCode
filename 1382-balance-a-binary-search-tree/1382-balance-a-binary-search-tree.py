# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        inorder = []
        self.inorderTraversal(root, inorder)
        return self.constructBBST(inorder, 0, len(inorder) - 1)
    
    def inorderTraversal(self, root, inorder):
        if not root:
            return
        self.inorderTraversal(root.left, inorder)
        inorder.append(root.val)
        self.inorderTraversal(root.right, inorder)
        
    def constructBBST(self, inorder, start, end):
        if start > end:
            return None
        mid = start + (end - start) // 2
        left = self.constructBBST(inorder, start, mid - 1)
        right = self.constructBBST(inorder, mid + 1, end)
        node = TreeNode(inorder[mid], left, right)
        return node