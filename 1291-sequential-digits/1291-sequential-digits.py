class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res = []
        temp = "123456789"
        for length in range(len(str(low)), len(str(high)) + 1):
            for i in range(10 - length):
                cur = int(temp[i: i + length])
                if low <= cur <= high:
                    res.append(cur)
        return res