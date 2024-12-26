class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total_sum = sum(nums)
        dp = [0] * (2 * total_sum + 1)
        
        dp[nums[0] + total_sum] = 1
        dp[-nums[0] + total_sum] += 1
        
        for index in range(1, len(nums)):
            next_dp = [0] * (2 * total_sum + 1)
            for sum_val in range(-total_sum, total_sum + 1):
                if dp[sum_val + total_sum] > 0:
                    next_dp[sum_val + nums[index] + total_sum] += dp[sum_val + total_sum]
                    next_dp[sum_val - nums[index] + total_sum] += dp[sum_val + total_sum]
            dp = next_dp
            
        return 0 if abs(target) > total_sum else dp[target + total_sum]