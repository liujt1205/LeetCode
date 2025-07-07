class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        highest = max(nums)
        stack = []
        for i in range(2 * n):
            cur = nums[i % n]
            while stack and cur > stack[-1][1]:
                index, _ = stack.pop()
                res[index] = cur
            
            if cur == highest and i < n:
                res[i] = -1
                continue

            if (not stack or cur <= stack[-1][1]) and i < n:
                stack.append((i, cur))

            if i >= n and cur == highest:
                break

        return res