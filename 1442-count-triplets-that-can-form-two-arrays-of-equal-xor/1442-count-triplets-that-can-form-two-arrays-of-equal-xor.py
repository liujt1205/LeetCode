class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        prefix = [0] * (n + 1)
        cur = 0
        for i in range(n):
            cur ^= arr[i]
            prefix[i + 1] = cur
            
        res = 0
        count = defaultdict(int)
        total = defaultdict(int)
        for i in range(n + 1):
            res += count[prefix[i]] * (i - 1) - total[prefix[i]]
            total[prefix[i]] += i
            count[prefix[i]] += 1
                    
        return res