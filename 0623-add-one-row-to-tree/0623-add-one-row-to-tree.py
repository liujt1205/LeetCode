# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            newRoot = TreeNode(val, root)
            return newRoot
        curDepth = 1
        queue = deque()
        queue.append(root)
        terminate = False;
        while queue:
            if curDepth == depth - 1:
                terminate = True
            for i in range(len(queue)):
                cur = queue.popleft()
                if terminate:
                    cur.left = TreeNode(val, cur.left)
                    cur.right = TreeNode(val, None, cur.right)
                else:
                    if cur.left:
                        queue.append(cur.left)
                    if cur.right:
                        queue.append(cur.right)
            curDepth += 1
        return root