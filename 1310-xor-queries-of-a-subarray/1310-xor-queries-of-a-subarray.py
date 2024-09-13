class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n = len(arr)
        pre = [0] * (n + 1)
        for i in range(n):
            pre[i + 1] = pre[i] ^ arr[i]
            
        res = [0] * len(queries)
        for i in range(len(queries)):
            left, right = queries[i]
            res[i] = pre[right + 1] ^ pre[left]
            
        return res