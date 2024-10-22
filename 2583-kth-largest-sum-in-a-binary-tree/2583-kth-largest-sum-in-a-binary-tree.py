# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        sums = []
        level = [root]
        while level:
            curSum = 0
            newLevel = []
            for i in range(len(level)):
                curSum += level[i].val
                if level[i].left:
                    newLevel.append(level[i].left)
                if level[i].right:
                    newLevel.append(level[i].right)
            sums.append(curSum)
            level = newLevel
            
        if k > len(sums):
            return -1
        else:
            sums.sort()
            return sums[-k]