class Solution:
    def kthLuckyNumber(self, k: int) -> str:
        k += 1
        binaryK = bin(k)[3:]
        res = ""
        for char in binaryK:
            if char == "1":
                res += "7"
            else:
                res += "4"
        return res