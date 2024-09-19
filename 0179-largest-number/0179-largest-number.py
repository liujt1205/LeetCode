class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        str_nums = []
        for num in nums:
            str_nums.append(str(num))
            
        str_nums.sort(key=lambda x: x * 10, reverse=True)
        if str_nums[0] == "0":
            return "0"
        return ''.join(str_nums)