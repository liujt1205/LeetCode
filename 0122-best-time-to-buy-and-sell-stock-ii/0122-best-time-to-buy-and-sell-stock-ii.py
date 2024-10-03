class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        buy = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < prices[i - 1]:
                res += prices[i - 1] - buy
                buy = prices[i]
                
        res += prices[-1] - buy
            
        return res