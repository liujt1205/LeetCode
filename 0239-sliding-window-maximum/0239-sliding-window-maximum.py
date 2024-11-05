class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        i = 0
        stack = deque()
        for i in range(k):
            while stack and stack[0] + k < i:
                stack.popleft()
            while stack and nums[i] >= nums[stack[-1]]:
                stack.pop()
            stack.append(i)

        res.append(nums[stack[0]])
            
        for i in range(k, len(nums)):
            while stack and stack[0] + k <= i:
                stack.popleft()
            while stack and nums[i] >= nums[stack[-1]]:
                stack.pop()
            stack.append(i)
            res.append(nums[stack[0]])
            
        return res