class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        memo = {}
        for num in nums:
            d = gcd(num, k)
            memo[d] = memo.get(d, 0) + 1
        res = 0
        for a in memo:
            for b in memo:
                if a <= b and a * b % k == 0:
                    if a == b:
                        res += memo[a] * (memo[b] - 1) // 2
                    else:
                        res += memo[a] * memo[b]
        return res
                    