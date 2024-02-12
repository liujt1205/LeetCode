class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        visited = [0] * n
        queue = deque()
        queue.append(start)
        while queue:
            cur = queue.popleft()
            if cur < 0 or cur >= n:
                continue
            if arr[cur] == 0:
                return True
            if visited[cur] == 0:
                visited[cur] = 1
                queue.append(cur - arr[cur])
                queue.append(cur + arr[cur])
        return False