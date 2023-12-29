class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        memo = [[float('inf')] * n + [0] for _ in range(d + 1)]
        for remaining_days in range(1, d + 1):
            for pre_task in range(n - remaining_days + 1):
                most = 0
                for end_task in range(pre_task + 1, n - remaining_days + 2):
                    most = max(most, jobDifficulty[end_task - 1])
                    memo[remaining_days][pre_task] = min(memo[remaining_days][pre_task], most + memo[remaining_days - 1][end_task])
        if memo[d][0] == float('inf'):
            return -1
        return memo[d][0]