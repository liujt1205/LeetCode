class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        n = len(nums)
        freq = [0] * (n + 1)
        count = 0
        res = 0
        left = 0
        curCount = 0
        for i in range(n):
            freq[nums[i]] += 1
            if freq[nums[i]] == 1:
                count += 1
            while count > k:
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    count -= 1
                left += 1
                curCount = 0
            if count == k:
                while freq[nums[left]] > 1:
                    freq[nums[left]] -= 1
                    curCount += 1
                    left += 1
                res += curCount + 1
        return res