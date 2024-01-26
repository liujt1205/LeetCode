class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        stack = []
        n = len(nums)
        res = 0
        for i in range(n + 1):
            while stack and (i == n or nums[stack[-1]] >= nums[i]):
                mid = stack.pop()
                if stack:
                    left = stack[-1]
                else:
                    left = -1
                res -= (mid - left) * (i - mid) * nums[mid]
            stack.append(i)
        stack.clear()
        for i in range(n + 1):
            while stack and (i == n or nums[stack[-1]] <= nums[i]):
                mid = stack.pop()
                if stack:
                    left = stack[-1]
                else:
                    left = -1
                res += (mid - left) * (i - mid) * nums[mid]
            stack.append(i)
        return res