class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        n = len(customers)
        nextStart = 0
        sumWait = 0
        for arrive, time in customers:
            if nextStart < arrive:
                nextStart = arrive
            nextStart += time
            sumWait += nextStart - arrive
        return sumWait / n