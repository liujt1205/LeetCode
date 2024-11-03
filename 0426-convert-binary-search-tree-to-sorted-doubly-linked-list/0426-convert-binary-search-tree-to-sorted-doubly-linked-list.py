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
        head.left = head
        head.right = head
        queue.append((root, head, head))
        while queue:
            node, p, n = queue.popleft()
            if node.left:
                queue.append((node.left, p, node))
            if node.right:
                queue.append((node.right, node, n))
            node.left = p
            node.right = n
            p.right = node
            n.left = node
            
        head.left.right = head.right
        head.right.left = head.left
        
        return head.right
        