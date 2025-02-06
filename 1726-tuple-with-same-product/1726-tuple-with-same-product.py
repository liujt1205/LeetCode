class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        res = 0
        mult = defaultdict(int)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if mult[nums[i] * nums[j]] != 0:
                    res += mult[nums[i] * nums[j]]
                
                mult[nums[i] * nums[j]] += 1

        return res * 8