# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:
        sign = 1
        curNum = 0
        haveNum = False
        stack = []
        for char in s:
            if char == "-":
                sign = -1
            elif char == '(':
                if haveNum:
                    newNode = TreeNode(curNum * sign)
                    stack.append(newNode)
                    sign = 1
                    curNum = 0
                    haveNum = False                    
            elif char == ')':
                if haveNum:
                    newNode = TreeNode(curNum * sign)
                    nextNode = stack.pop()
                    if not nextNode.left:
                        nextNode.left = newNode
                    else:
                        nextNode.right = newNode
                    stack.append(nextNode)
                    haveNum = False
                    sign = 1
                    curNum = 0
                else:
                    curNode = stack.pop()
                    nextNode = stack.pop()
                    if not nextNode.left:
                        nextNode.left = curNode
                    else:
                        nextNode.right = curNode
                    stack.append(nextNode)
            else:
                curNum = curNum * 10 + int(char)
                haveNum = True
        if haveNum:
            newNode = TreeNode(curNum * sign)
            stack.append(newNode)
                
        return stack.pop() if stack else None