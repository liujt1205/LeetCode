# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        stack = []
        num = 0
        count = 0
        prev = 0
        root = TreeNode(-1)
        for char in traversal:
            if char.isdigit():
                num = num * 10 + int(char)
            else:
                if prev == '-':
                    count += 1
                else:
                    while stack and stack[-1][1] != count - 1:
                        stack.pop()
                
                    curNode = TreeNode(num)
                    if not stack:
                        root = curNode
                    elif not stack[-1][0].left:
                        stack[-1][0].left = curNode
                    else:
                        stack[-1][0].right = curNode

                    stack.append((curNode, count))
                    count = 1
                    num = 0
            prev = char

        while stack and stack[-1][1] != count - 1:
            stack.pop()
    
        curNode = TreeNode(num)
        if not stack:
            root = curNode
        elif not stack[-1][0].left:
            stack[-1][0].left = curNode
        else:
            stack[-1][0].right = curNode

        return root
        
