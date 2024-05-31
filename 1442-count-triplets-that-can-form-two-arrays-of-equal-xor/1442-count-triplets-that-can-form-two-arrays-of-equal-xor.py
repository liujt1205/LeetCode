class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        prefix = [0] * (n + 1)
        cur = 0
        for i in range(n):
            cur ^= arr[i]
            prefix[i + 1] = cur
            
        res = 0
        for k in range(1, n):
            for i in range(k):
                if prefix[i] == prefix[k + 1]:
                    res += k - i
                    
        return res