class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0:
            return
        red = 0
        blue = len(nums) - 1
        cur = 0
        while cur <= blue:
            if nums[cur] == 0:
                nums[cur] = nums[red]
                nums[red] = 0
                red += 1
                cur += 1
            elif nums[cur] == 1:
                cur += 1
            else:
                nums[cur] = nums[blue]
                nums[blue] = 2
                blue -= 1
                