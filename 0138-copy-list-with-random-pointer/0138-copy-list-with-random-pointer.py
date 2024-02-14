"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        node = head
        while node != None:
            copy = Node(node.val, node.next, None)
            node.next = copy
            node = copy.next
        newHead = head.next
        node = head
        while node != None:
            if node.random:
                node.next.random = node.random.next
            node = node.next.next
        node = head
        newNode = newHead
        while node:
            node.next = node.next.next
            if newNode.next:
                newNode.next = newNode.next.next
            node = node.next
            newNode = newNode.next
        return newHead
            