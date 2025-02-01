class Solution:
    def distinctNumbers(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        count = defaultdict(int)
        distinct = 0
        for i in range(k):
            if count[nums[i]] == 0:
                distinct += 1
            count[nums[i]] += 1
            
        res = []
        res.append(distinct)
        for i in range(k, n):
            count[nums[i - k]] -= 1
            if count[nums[i - k]] == 0:
                distinct -= 1
            
            count[nums[i]] += 1
            if count[nums[i]] == 1:
                distinct += 1
            res.append(distinct)

        return res