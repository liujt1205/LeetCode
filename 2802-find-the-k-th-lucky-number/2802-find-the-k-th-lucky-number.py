class Solution:
    def kthLuckyNumber(self, k: int) -> str:
        k += 1
        binaryK = bin(k)[3:]
        res = binaryK.replace("0", "4").replace("1", "7")
        return res