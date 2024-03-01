class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        n = len(s)
        count = 0
        for char in s:
            if char == '1':
                count += 1
        return '1' * (count - 1) + '0' * (n - count) + '1'