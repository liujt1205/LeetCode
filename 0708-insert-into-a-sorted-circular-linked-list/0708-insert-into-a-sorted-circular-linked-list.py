"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        if not head:
            newNode = Node(insertVal)
            newNode.next = newNode
            return newNode
        
        if head.next == head:
            newNode = Node(insertVal, head)
            head.next = newNode
            return head
            
        def check(node, insertVal):
            return node.val == insertVal or (node.next.val < node.val and node.next.val > insertVal) or (node.next.val < node.val and node.val < insertVal) or (node.val < insertVal and node.next.val > insertVal)
            
        cur = head.next
        while cur != head:
            if check(cur, insertVal):
                newNode = Node(insertVal, cur.next)
                cur.next = newNode
                break
            else:
                cur = cur.next
                
        if cur.next.val != insertVal:
            newNode = Node(insertVal, cur.next)
            cur.next = newNode
                
        return head
