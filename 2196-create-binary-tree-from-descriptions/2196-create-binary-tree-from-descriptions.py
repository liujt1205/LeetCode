# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = {}
        nonRoot = set()
        for parent, child, isLeft in descriptions:
            parentNode = nodes.get(parent, TreeNode(parent))
            childNode = nodes.get(child, TreeNode(child))
            if isLeft:
                parentNode.left = childNode
            else:
                parentNode.right = childNode
            nodes[parent] = parentNode
            nodes[child] = childNode
            nonRoot.add(child)
        for node in nodes.values():
            if node.val not in nonRoot:
                return node