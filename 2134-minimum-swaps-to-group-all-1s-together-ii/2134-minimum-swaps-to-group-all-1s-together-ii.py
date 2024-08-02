class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        nums.extend(nums[:])
        count = [0] * (2 * n + 1)
        total = 0
        for i in range(2 * n):
            if nums[i] == 0:
                count[i + 1] = count[i] + 1
            else:
                count[i + 1] = count[i]
                total += 1
        total = total // 2
        res = total
        print(count)
        
        for i in range(2 * n - total):
            res = min(res, count[i + total] - count[i])
            
        return res