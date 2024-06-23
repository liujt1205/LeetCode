class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        res = 0
        small = deque()
        large = deque()
        start = -1
        for i in range(len(nums)):
            while large and large[-1][0] <= nums[i]:
                large.pop()
            large.append((nums[i], i))
            while small and small[-1][0] >= nums[i]:
                small.pop()
            small.append((nums[i], i))
            while large[0][0] - small[0][0] > limit:
                if large[0][1] < small[0][1]:
                    pre = large.popleft()
                    start = pre[1]
                else:
                    pre = small.popleft()
                    start = pre[1]
            res = max(res, i - start)
        return res