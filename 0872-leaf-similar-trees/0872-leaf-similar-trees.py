# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        sq1 = deque()
        def dfs(root: Optional[TreeNode]):
            if root is None:
                return
            if root.left is None and root.right is None:
                sq1.append(root.val)
            else:
                dfs(root.left)
                dfs(root.right)
        dfs(root1)
        stack = []
        stack.append(root2)
        while len(stack) != 0:
            curNode = stack.pop()
            if curNode is None:
                continue
            if curNode.left is None and curNode.right is None:
                if not sq1 or curNode.val != sq1.popleft():
                    return False
            else:
                stack.append(curNode.right)
                stack.append(curNode.left)
        return not sq1
                
            