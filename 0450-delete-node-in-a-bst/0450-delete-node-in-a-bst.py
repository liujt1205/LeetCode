# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:       
        if root:
            if root.val < key:
                root.right = self.deleteNode(root.right, key)
            elif root.val > key:
                root.left = self.deleteNode(root.left, key)
            elif not root.left:
                root = root.right
            elif not root.right:
                root = root.left
            else:
                root.val = self.findPredVal(root)
                root.left = self.deleteNode(root.left, root.val)
        return root
    
    def findPredVal(self, node):
        pred = node.left
        while pred.right:
            pred = pred.right
        return pred.val