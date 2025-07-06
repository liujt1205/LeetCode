class Solution:
    def findCoins(self, numWays: List[int]) -> List[int]:
        N = len(numWays)
        dp = [0] * (N + 1)
        dp[0] = 1
        
        coins = []
        for i in range(1, N + 1):
            target = numWays[i - 1]
        
            if dp[i] == target - 1:
                coins.append(i)
                for j in range(i, N + 1):
                    dp[j] += dp[j - i]
            if dp[i] != target:
                return []
        
        return coins
