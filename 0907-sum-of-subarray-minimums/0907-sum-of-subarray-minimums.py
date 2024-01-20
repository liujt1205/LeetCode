class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        stack = []
        mod = 1000000007
        res = 0
        for i in range(len(arr) + 1):
            while stack and (i == len(arr) or arr[stack[-1]] >= arr[i]):
                mid = stack.pop()
                right_boundary = i
                if not stack:
                    left_boundary = -1
                else: 
                    left_boundary = stack[-1]
                count = (mid - left_boundary) * (right_boundary - mid)
                res += count * arr[mid]
            stack.append(i)
        return res % mod