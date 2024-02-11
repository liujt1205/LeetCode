class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)
        def check(target):
            res = 1
            cur = 0
            for weight in weights:
                cur += weight
                if cur > target:
                    res += 1
                    cur = weight
            return res
        while left < right:
            mid = (left + right) // 2
            if check(mid) <= days:
                right = mid
            else:
                left = mid + 1
        return left