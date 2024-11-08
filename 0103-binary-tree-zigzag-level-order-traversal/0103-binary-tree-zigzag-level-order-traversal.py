# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        queue = deque([root])
        if not root:
            return res
        level = 0
        while queue:
            queue_size = len(queue)
            level_list = []
            newQueue = deque()
            for i in range(queue_size):
                cur = queue.popleft()
                if not cur:
                    continue
                level_list.append(cur.val)
                if level % 2 == 0:
                    newQueue.appendleft(cur.left)
                    newQueue.appendleft(cur.right)
                else:
                    newQueue.appendleft(cur.right)
                    newQueue.appendleft(cur.left)
            level += 1
            if level_list:
                res.append(level_list)
            queue = newQueue
            
        return res
        
                
            
        