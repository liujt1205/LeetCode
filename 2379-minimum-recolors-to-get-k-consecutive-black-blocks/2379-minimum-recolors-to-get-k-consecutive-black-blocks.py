class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        cur = 0
        for i in range(k):
            if blocks[i] == 'W':
                cur += 1

        res = cur
        for i in range(k, len(blocks)):
            if blocks[i] == 'W':
                cur += 1
            if blocks[i - k] == 'W':
                cur -= 1

            res = min(res, cur)

        return res