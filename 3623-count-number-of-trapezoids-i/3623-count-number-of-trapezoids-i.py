class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        mod = 1000000007

        count = defaultdict(int)
        for x, y in points:
            count[y] += 1

        res = 0
        comb = 0
        
        for num in count.values():
            diff = num * (num - 1) // 2
            res = (res + comb * diff) % mod
            comb = (comb + diff) % mod

        return res