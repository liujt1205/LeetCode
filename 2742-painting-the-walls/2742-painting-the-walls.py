class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(cost)
        time, cost = zip(*sorted(zip(time, cost)))
        memo = [float('inf')] * (n + 1)
        memo[0] = 0
        for i in range(n):
            curTime, curCost = time[i], cost[i]
            curMemo = memo[:]
            for j in range(n + 1):
                if j + curTime + 1 > n:
                    curMemo[n] = min(curMemo[n], memo[j] + curCost)
                else:
                    curMemo[j + curTime + 1] = min(memo[j + curTime + 1], memo[j] + curCost)
            memo = curMemo[:]
        return memo[n]