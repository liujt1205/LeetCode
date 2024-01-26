class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        possible = [0] * (total // 2 + 1)
        possible[0] = 1
        for stone in stones:
            new = possible[:]
            for i in range(total // 2 + 1):
                if possible[i] == 1 and i + stone <= total // 2:
                    new[i + stone] = 1
            possible = new
        for i in range(total // 2, -1, -1):
            if possible[i] == 1:
                return total - i * 2