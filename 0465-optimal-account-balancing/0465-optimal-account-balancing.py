class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        balance = [0] * 12
        for i, j, amount in transactions:
            balance[j] += amount
            balance[i] -= amount
        remaining = []
        for num in balance:
            if num:
                remaining.append(num)
        n = len(remaining)
        def dfs(cur):
            while cur < n and not remaining[cur]:
                cur += 1
            if cur == n:
                return 0
            cost = float('inf')
            for nxt in range(cur + 1, n):
                if remaining[nxt] * remaining[cur] < 0:
                    remaining[nxt] += remaining[cur]
                    cost = min(cost, 1 + dfs(cur + 1))
                    remaining[nxt] -= remaining[cur]
            return cost
        
        return dfs(0)