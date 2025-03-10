class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        if len(colors) < k:
            return 0

        ref = colors + colors[:k - 1]
        last = -1
        res = 0
        for i in range(len(ref) - 1):
            if ref[i] == ref[i + 1]:
                last = i
            if i >= k - 2 and last < i - k + 2:
                res += 1

        return res
        