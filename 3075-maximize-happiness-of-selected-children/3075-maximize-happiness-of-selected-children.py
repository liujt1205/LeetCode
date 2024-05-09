class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness = sorted(happiness, reverse = True)
        count = 0
        res = 0
        for i in range(len(happiness)):
            res += max(happiness[i] - count, 0)
            count += 1
            if count == k or count >= happiness[i]:
                break
        return res