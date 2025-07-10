class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()
        n = len(events)
        dp = [[0] * (n + 1) for _ in range(k + 1)]
        starts = [start for start, end, value in events]

        for count in range(1, k + 1):
            for i in range(n - 1, -1, -1):
                next_i = bisect_right(starts, events[i][1])
                dp[count][i] = max(dp[count][i + 1], events[i][2] + dp[count - 1][next_i])

        return dp[k][0]