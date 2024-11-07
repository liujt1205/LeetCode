class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff = float("inf")
        nums.sort()
        for i in range(len(nums)):
            lo, hi = i + 1, len(nums) - 1
            while lo < hi:
                cur_sum = nums[i] + nums[lo] + nums[hi]
                if abs(target - cur_sum) < abs(diff):
                    diff = target - cur_sum
                if cur_sum < target:
                    lo += 1
                else:
                    hi -= 1
            if diff == 0:
                break
        return target - diff