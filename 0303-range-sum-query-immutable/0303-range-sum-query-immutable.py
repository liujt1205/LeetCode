class NumArray:

    def __init__(self, nums: List[int]):
        self.memo = nums
        self.sums = []

    def sumRange(self, left: int, right: int) -> int:
        n = len(self.sums)
        if n:
            curSum = self.sums[n - 1]
        else:
            curSum = 0
        if right >= n:
            for i in range(n, right + 1):
                curSum += self.memo[i]
                self.sums.append(curSum)
        if left:
            return self.sums[right] - self.sums[left - 1]
        else:
            return self.sums[right]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)