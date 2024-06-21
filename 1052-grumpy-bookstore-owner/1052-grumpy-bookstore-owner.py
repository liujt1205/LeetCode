class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        diff = [0] * n
        total = 0
        for i in range(n):
            diff[i] += grumpy[i] * customers[i]
            total += (1- grumpy[i]) * customers[i]
            
        change = 0
        for i in range(minutes):
            change += diff[i]
        best = change
        for i in range(minutes, n):
            change += diff[i] - diff[i - minutes]
            best = max(best, change)
        return total + best