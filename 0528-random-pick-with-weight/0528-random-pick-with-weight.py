class Solution:

    def __init__(self, w: List[int]):
        self.prefix_sum = []
        cur_sum = 0
        for weight in w:
            cur_sum += weight
            self.prefix_sum.append(cur_sum)
        self.total = cur_sum

    def pickIndex(self) -> int:
        target = self.total * random.random()
        low, high = 0, len(self.prefix_sum)
        while low < high:
            mid = low + (high - low) // 2
            if target > self.prefix_sum[mid]:
                low = mid + 1
            else:
                high = mid
        return low


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()