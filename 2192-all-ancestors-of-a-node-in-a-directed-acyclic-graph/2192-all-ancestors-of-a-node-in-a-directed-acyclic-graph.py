class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        freq = [0] * n
        children = [set() for _ in range(n)]
        res = [set() for _ in range(n)]
        for start, end in edges:
            freq[end] += 1
            children[start].add(end)
        queue = deque()
        for i in range(n):
            if freq[i] == 0:
                queue.append(i)
        while queue:
            cur = queue.popleft()
            for child in children[cur]:
                res[child].update(res[cur])
                res[child].add(cur)
                freq[child] -= 1
                if freq[child] == 0:
                    queue.append(child)
        return [sorted(list(ans)) for ans in res]