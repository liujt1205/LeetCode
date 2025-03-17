class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        count = defaultdict(int)
        odd = 0
        for num in nums:
            count[num] += 1
            if count[num] % 2 == 0:
                odd -= 1
            else:
                odd += 1

        return odd == 0