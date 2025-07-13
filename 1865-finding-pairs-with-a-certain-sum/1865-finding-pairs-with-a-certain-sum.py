class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.count1 = Counter(nums1)
        self.count2 = Counter(nums2)

    def add(self, index: int, val: int) -> None:
        prev = self.nums2[index]
        self.count2[prev] -= 1
        self.nums2[index] += val
        self.count2[prev + val] += 1

    def count(self, tot: int) -> int:
        res = 0
        for num in self.count1:
            res += self.count1[num] * self.count2[tot - num]

        return res


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)