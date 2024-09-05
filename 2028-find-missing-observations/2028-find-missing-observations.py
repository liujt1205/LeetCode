class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        total = sum(rolls)
        m = len(rolls)
        target = mean * (m + n)
        
        if target - total < n or target - total > 6 * n:
            return []
        
        base, add = (target - total) // n, (target - total) % n
        res = [base] * n
        for i in range(add):
            res[i] += 1
        
        return res