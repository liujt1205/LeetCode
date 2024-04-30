class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        final = 0
        for num in nums:
            final ^= num
        return bin(final ^ k).count('1')