class Solution:
    def findComplement(self, num: int) -> int:
        bit = 1
        while num >= bit:
            num = num ^ bit
            bit = bit << 1
            
        return num