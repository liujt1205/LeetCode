class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        i = 0
        stack = deque()
        while i < k - 1:
            while stack and nums[i] >= nums[stack[-1]]:
                stack.pop()
            if not stack or nums[i] < nums[stack[-1]]:
                stack.append(i)
            while stack and stack[0] + k < i:
                stack.popleft()
            i += 1
            
        while i < len(nums):
            while stack and nums[i] >= nums[stack[-1]]:
                stack.pop()
            if not stack or nums[i] < nums[stack[-1]]:
                stack.append(i)
            while stack and stack[0] + k <= i:
                stack.popleft()
            i += 1
            res.append(nums[stack[0]])
            
        return res