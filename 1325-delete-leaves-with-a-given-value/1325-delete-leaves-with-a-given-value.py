# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def checkLeaf(node, target):
            if node.left is not None:
                node.left = node.left if not checkLeaf(node.left, target) else None
            if node.right is not None:
                node.right = node.right if not checkLeaf(node.right, target) else None
            if node.left is None and node.right is None and node.val == target:
                return True
            return False
        
        if checkLeaf(root, target):
            return None
        else:
            return root
