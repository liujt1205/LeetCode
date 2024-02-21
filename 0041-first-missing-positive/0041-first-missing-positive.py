class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        def log(num):
            if 0 < num <= n:
                temp = nums[num - 1]
                nums[num - 1] = float('inf')
                if temp != float('inf'):
                    log(temp)
        for num in nums:
            if num != float('inf'):
                log(num)
        for i in range(n):
            if nums[i] != float('inf'):
                return i + 1
        return n + 1