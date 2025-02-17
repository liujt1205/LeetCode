class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        counts = [0] * 26
        for char in tiles:
            counts[ord(char) - ord('A')] += 1

        def count_sequence(counts):
            res = 0
            for i in range(26):
                if counts[i] == 0:
                    continue

                res += 1
                counts[i] -= 1
                res += count_sequence(counts)
                counts[i] += 1

            return res

        return count_sequence(counts)