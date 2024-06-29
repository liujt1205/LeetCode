# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def splitBST(self, root: Optional[TreeNode], target: int) -> List[Optional[TreeNode]]:
        rootSM = TreeNode(0)
        rootLG = TreeNode(0)
        curSM = rootSM
        curLG = rootLG
        cur = root
        nextNode = None
        while cur:
            if cur.val <= target:
                curSM.right = cur
                curSM = cur
                nextNode = cur.right
                curSM.right = None
            else:
                curLG.left = cur
                curLG = cur
                nextNode = cur.left
                curLG.left = None
            cur = nextNode
        return [rootSM.right, rootLG.left]