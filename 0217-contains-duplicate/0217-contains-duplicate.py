class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        memo = {}
        for num in nums:
            if memo.get(num, True):
                memo[num] = False
            else:
                return True
        return False