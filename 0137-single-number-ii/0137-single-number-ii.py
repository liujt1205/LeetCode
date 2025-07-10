class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for shift in range(32):
            bit_sum = 0
            for num in nums:
                cur_bit = num >> shift & 1
                bit_sum += cur_bit

            loner_bit = bit_sum % 3
            res = res | (loner_bit << shift)

        if res >= (1 << 31):
            res = res - (1 << 32)

        return res