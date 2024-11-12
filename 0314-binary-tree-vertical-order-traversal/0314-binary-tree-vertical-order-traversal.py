# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        memo = defaultdict(list)
        queue = deque()
        queue.append((root, 0))
        left, right = 0, 0
        while queue:
            cur = queue.popleft()
            memo[cur[1]].append(cur[0].val)
            left = min(left, cur[1])
            right = max(right, cur[1])
            if cur[0].left:
                queue.append((cur[0].left, cur[1]-1))
            if cur[0].right:
                queue.append((cur[0].right, cur[1]+1))
        res = []
        
        for i in range(left, right + 1):
            res.append(memo[i])
        return res