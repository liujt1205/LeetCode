class Solution:
    def maximumProfit(self, present: List[int], future: List[int], budget: int) -> int:
        memo = [-1] * (budget + 1)
        memo[0] = 0
        present, future = zip(*sorted(zip(present, future)))
        for i in range(len(present)):
            curPrice = present[i]
            profit = future[i] - curPrice
            curMemo = memo[:]
            for i in range(budget + 1):
                if curPrice + i <= budget and memo[i] != -1:
                    curMemo[curPrice + i] = max(memo[curPrice + i], profit + memo[i])
            memo = curMemo[:]
        res = 0
        for i in range(budget + 1):
            res = max(res, memo[i])
        return res
            