# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        queue = deque()
        queue.append(root)
        res = 0
        while queue:
            curNode = queue.popleft()
            if curNode is not None:
                curVal = curNode.val
                if curVal >= high:
                    queue.append(curNode.left)
                elif curVal <= low:
                    queue.append(curNode.right)
                else:
                    queue.append(curNode.left)
                    queue.append(curNode.right)
                if curVal <= high and curVal >= low:
                    res += curVal
        return res
        