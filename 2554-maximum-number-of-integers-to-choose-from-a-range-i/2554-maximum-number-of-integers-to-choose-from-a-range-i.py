class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned_set = set(banned)
        res = 0
        for i in range(1, n + 1):
            if i not in banned_set:
                maxSum -= i
                if maxSum >= 0:
                    res += 1
                    
        return res