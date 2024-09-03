class Solution:
    def getLucky(self, s: str, k: int) -> int:
        res = "".join(str(ord(c) - ord('a') + 1) for c in s)
        while k > 0:
            res = str(sum(int(num) for num in res))
            k -= 1
        return int(res)
        