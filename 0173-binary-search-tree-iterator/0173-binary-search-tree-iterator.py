# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.memo = []
        self.index = -1
        self.parseNode(root)

    def next(self) -> int:
        self.index += 1
        return self.memo[self.index]

    def hasNext(self) -> bool:
        return self.index != len(self.memo) - 1
    
    def parseNode(self, root):
        if not root:
            return
        if root.left:
            self.parseNode(root.left)
        
        self.memo.append(root.val)
        if root.right:
            self.parseNode(root.right)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()