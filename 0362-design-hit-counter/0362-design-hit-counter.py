class HitCounter:

    def __init__(self):
        self.memo = deque()

    def hit(self, timestamp: int) -> None:
        self.memo.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        while self.memo and self.memo[0] <= timestamp - 300:
            self.memo.popleft()
        
        return len(self.memo)


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)