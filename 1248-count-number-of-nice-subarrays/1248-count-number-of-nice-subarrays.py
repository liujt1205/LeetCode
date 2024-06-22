class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        odds = deque()
        odds.append(-1)
        res = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 1:
                if len(odds) > k:
                    pre = odds.popleft()
                    res += (odds[0] - pre) * (i - odds[-1])
                odds.append(i)
        if len(odds) > k:
            pre = odds.popleft()
            res += (odds[0] - pre) * (len(nums) - odds[-1])
        return res