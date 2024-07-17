# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        res = []
        delete_set = set(to_delete)
        pending = deque([root])
        while pending:
            node = pending.popleft()
            if not node:
                continue
            elif node.val in delete_set:
                pending.append(node.left)
                pending.append(node.right)
                continue
            else:
                res.append(node)
            queue = deque([(node, None, None)])
            while queue:
                info = queue.popleft()
                cur, parent, left = info[0], info[1], info[2]
                if not cur:
                    continue
                elif cur.val in delete_set:
                    if left:
                        parent.left = None
                    else:
                        parent.right = None
                    pending.append(cur.left)
                    pending.append(cur.right)
                else:
                    queue.append((cur.left, cur, True))
                    queue.append((cur.right, cur, False))
        return res
            
        