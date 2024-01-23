class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        memo = []
        res = 0
        for i in range(len(sticks)):
            heapq.heappush(memo, sticks[i])
        while len(memo) > 1:
            first = heapq.heappop(memo)
            second = heapq.heappop(memo)
            result = first + second
            res += result
            heapq.heappush(memo, result)
        return res