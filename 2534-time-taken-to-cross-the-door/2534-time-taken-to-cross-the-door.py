class Solution:
    def timeTaken(self, arrival: List[int], state: List[int]) -> List[int]:
        n = len(arrival)
        enter = []
        ex = []
        answer = [0] * n
        i = 0
        pre = 1
        for time in range(2 * n + 2):
            while i < n and arrival[i] <= time:
                if state[i] == 0:
                    heapq.heappush(enter, i)
                else:
                    heapq.heappush(ex, i)
                i += 1
            if not enter and not ex:
                pre = 1
                if i == n:
                    break
            elif not enter or (ex and pre == 1):
                cur = heapq.heappop(ex)
                answer[cur] = time
                pre = 1
            elif not ex or (enter and pre == 0):
                cur = heapq.heappop(enter)
                answer[cur] = time
                pre = 0
        return answer