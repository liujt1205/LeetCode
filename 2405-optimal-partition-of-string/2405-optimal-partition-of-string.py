class Solution:
    def partitionString(self, s: str) -> int:
        start = 0
        length = 0
        seen = set()
        res = 0
        while start + length < len(s):
            seen.add(s[start + length])
            length += 1
            if len(seen) < length:
                res += 1
                seen.clear()
                start = start + length - 1
                length = 1
                seen.add(s[start + length - 1])

        return res + 1