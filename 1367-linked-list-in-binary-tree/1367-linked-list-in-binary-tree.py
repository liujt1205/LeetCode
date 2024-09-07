# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def verify(listNode, treeNode):
            if listNode is None:
                return True
            if treeNode.left and treeNode.left.val == listNode.val:
                result = verify(listNode.next, treeNode.left)
                if result:
                    return True
            if treeNode.right and treeNode.right.val == listNode.val:
                result = verify(listNode.next, treeNode.right)
                if result:
                    return True
            return False
        
        queue = deque()
        queue.append(root)
        while queue:
            cur = queue.popleft()
            if cur is None:
                continue
            if cur.val == head.val:
                result = verify(head.next, cur)
                if result:
                    return True
            queue.append(cur.left)
            queue.append(cur.right)
        return False