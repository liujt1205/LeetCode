# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        res = [root.val]
        def getLeftBoundary(node):
            if not node:
                return None
            if node.left or node.right:
                res.append(node.val)
            else:
                return None
            if node.left:
                getLeftBoundary(node.left)
            else:
                getLeftBoundary(node.right)
                
        getLeftBoundary(root.left)
        
        def getLeaf(node):
            if not node:
                return
            if not node.left and not node.right and node != root:
                res.append(node.val)
            if node.left:
                getLeaf(node.left)
            if node.right:
                getLeaf(node.right)
                
        getLeaf(root)
        
        def getRightBoundary(node):
            if not node:
                return None
            if not node.left and not node.right:
                return None
            if node.right:
                getRightBoundary(node.right)
            elif node.left:
                getRightBoundary(node.left)
            res.append(node.val)
            
        getRightBoundary(root.right)
        return res