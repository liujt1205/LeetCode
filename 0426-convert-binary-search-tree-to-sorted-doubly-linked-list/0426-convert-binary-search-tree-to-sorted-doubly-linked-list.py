"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        
        head = Node(-1)
        queue = deque()        
        listNode = Node(root.val, head, head)
        head.right = listNode
        head.left = listNode
        queue.append((root, listNode))
        
        while queue:
            treenode, dllnode = queue.popleft()
            if treenode.left:
                newNode = Node(treenode.left.val, dllnode.left, dllnode)
                dllnode.left.right = newNode
                dllnode.left = newNode
                queue.append((treenode.left, newNode))
            if treenode.right:
                newNode = Node(treenode.right.val, dllnode, dllnode.right)
                dllnode.right.left = newNode
                dllnode.right = newNode
                queue.append((treenode.right, newNode))
                
        head.right.left = head.left
        head.left.right = head.right
        return head.right