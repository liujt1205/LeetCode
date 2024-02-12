class MedianFinder:

    def __init__(self):
        self.pqMin = []
        self.pqMax = []
        
    def balance(self):
        if len(self.pqMax) - len(self.pqMin) > 1:
            cur = -heapq.heappop(self.pqMax)
            heapq.heappush(self.pqMin, cur)
        elif len(self.pqMin) - len(self.pqMax) > 1:
            cur = heapq.heappop(self.pqMin)
            heapq.heappush(self.pqMax, -cur)

    def addNum(self, num: int) -> None:
        if not self.pqMin:
            self.pqMin.append(num)
        else:
            bigger = self.pqMin[0]
            if num >= bigger:
                heapq.heappush(self.pqMin, num)
                self.balance()
            else:
                heapq.heappush(self.pqMax, -num)
                self.balance()
                

    def findMedian(self) -> float:
        if not self.pqMax:
            return self.pqMin[0]
        elif not self.pqMin:
            return self.pqMax[0]
        else:
            if len(self.pqMax) > len(self.pqMin):
                return -self.pqMax[0]
            elif len(self.pqMax) < len(self.pqMin):
                return self.pqMin[0]
            else:
                return (self.pqMin[0] - self.pqMax[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()