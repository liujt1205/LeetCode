# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        graph = {}
        visited = deque()
        visited.append(root)
        while len(visited) != 0:
            curNode = visited.popleft()
            if curNode:
                visited.append(curNode.left)
                visited.append(curNode.right)
                linked = graph.get(curNode.val, set())
                if curNode.left:
                    linked.add(curNode.left.val)
                    child = graph.get(curNode.left.val, set())
                    child.add(curNode.val)
                    graph[curNode.left.val] = child
                if curNode.right:
                    linked.add(curNode.right.val)
                    child = graph.get(curNode.right.val, set())
                    child.add(curNode.val)
                    graph[curNode.right.val] = child
                graph[curNode.val] = linked
        BFS = deque()
        res = 0
        BFS.append((start, 0))
        infected = set()
        infected.add(start)
        
        while len(BFS) != 0:
            curNode, curTime = BFS.popleft()
            infected.add(curNode)
            res = max(res, curTime)
            for value in graph[curNode]:
                if value not in infected:
                    BFS.append((value, curTime + 1))
        return res