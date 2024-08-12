class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self._pq = []
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        heapq.heappush(self._pq, val)
        if len(self._pq) > self.k:
            heapq.heappop(self._pq)
        return self._pq[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)