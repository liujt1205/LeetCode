# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        queue = deque([root])
        levelSum = []
        while queue:
            curSum = 0
            levelSize = len(queue)
            for _ in range(levelSize):
                curNode = queue.popleft()
                curSum += curNode.val
                if curNode.left:
                    queue.append(curNode.left)
                if curNode.right:
                    queue.append(curNode.right)
            levelSum.append(curSum)
            
        queue.append(root)
        level = 1
        root.val = 0
        while queue:
            levelSize = len(queue)
            for _ in range(levelSize):
                curNode = queue.popleft()
                leftChild = 0 if not curNode.left else curNode.left.val
                rightChild = 0 if not curNode.right else curNode.right.val
                if curNode.left:
                    curNode.left.val = levelSum[level] - leftChild - rightChild
                    queue.append(curNode.left)
                if curNode.right:
                    curNode.right.val = levelSum[level] - leftChild - rightChild
                    queue.append(curNode.right)
            level += 1
                
        
        return root