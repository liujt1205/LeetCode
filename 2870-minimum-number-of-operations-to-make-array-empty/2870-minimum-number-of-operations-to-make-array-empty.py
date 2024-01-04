class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res = 0
        nums.sort()
        count = 0
        pre = float('inf')
        for num in nums:
            if num == pre:
                count += 1
            else:
                if count == 1:
                    return -1
                res += count // 3 + (1 if count % 3 != 0 else 0)
                pre = num
                count = 1
        if count == 1:
            return -1
        res += count // 3 + (1 if count % 3 != 0 else 0)
        return res