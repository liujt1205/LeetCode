class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        target_count = collections.Counter(target)
        overlap = [collections.Counter(sticker) & target_count
             for sticker in stickers]

        for i in range(len(overlap) - 1, -1, -1):
            if any(overlap[i] == overlap[i] & overlap[j] for j in range(len(overlap)) if i != j):
                overlap.pop(i)

        stickers = ["".join(sticker_count.elements()) for sticker_count in overlap]
        dp = [-1] * (1 << len(target))
        dp[0] = 0
        for state in range(1 << len(target)):
            if dp[state] == -1: continue
            for sticker in stickers:
                now = state
                for letter in sticker:
                    for i, c in enumerate(target):
                        if (now >> i) & 1: continue
                        if c == letter:
                            now |= 1 << i
                            break
                if dp[now] == -1 or dp[now] > dp[state] + 1:
                    dp[now] = dp[state] + 1

        return dp[-1]