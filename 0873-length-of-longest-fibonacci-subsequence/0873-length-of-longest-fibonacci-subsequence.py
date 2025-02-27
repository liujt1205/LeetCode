class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [[0] * n for _ in range(n)]
        res = 0

        for cur in range(2, n):
            start = 0
            end = cur - 1
            while start < end:
                cur_sum = arr[start] + arr[end]
                if cur_sum > arr[cur]:
                    end -= 1
                elif cur_sum < arr[cur]:
                    start += 1
                else:
                    dp[end][cur] = dp[start][end] + 1
                    res = max(res, dp[end][cur])
                    end -= 1
                    start += 1

        return res + 2 if res else 0