# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parents = {}
        def traverseTree(node, parent):
            parents[node.val] = parent
            if node.left:
                traverseTree(node.left, node)
            if node.right:
                traverseTree(node.right, node)
                
        traverseTree(root, None)
        visited = set()
        res = []
        def findNode(node, distance):
            if not node:
                return
            visited.add(node.val)
            if distance == k:
                res.append(node.val)
                return
            
            if node.left and node.left.val not in visited:
                findNode(node.left, distance + 1)
                
            if node.right and node.right.val not in visited:
                findNode(node.right, distance + 1)
                
            if parents[node.val] and parents[node.val].val not in visited:
                findNode(parents[node.val], distance + 1)
                
        findNode(target, 0)
        return res