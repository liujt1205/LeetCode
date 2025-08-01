class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        depth = cur = 0
        for c in seq:
            if c == '(':
                cur += 1
                depth = max(depth, cur)
            else:
                cur -= 1
        half = depth / 2
        res = [0] * len(seq)
        for i, c in enumerate(seq):
            if c == '(':
                cur += 1
                if cur > half: res[i] = 1
            else:
                if cur > half: res[i] = 1
                cur -= 1
        return res