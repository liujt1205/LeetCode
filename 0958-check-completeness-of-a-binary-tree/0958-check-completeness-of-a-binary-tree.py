# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        
        findEmpty = False
        queue = deque([root])
        while queue:
            size = len(queue)
            for i in range(size):
                curNode = queue.popleft()
                if not curNode.left:
                    findEmpty = True
                elif findEmpty:
                    return False
                else:
                    queue.append(curNode.left)
                    
                if not curNode.right:
                    findEmpty = True
                elif findEmpty:
                    return False
                else:
                    queue.append(curNode.right)
                    
        return True
                    