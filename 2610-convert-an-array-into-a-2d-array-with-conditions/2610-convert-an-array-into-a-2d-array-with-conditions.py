class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        memo = {}
        highest = 0
        for num in nums:
            memo[num] = memo.get(num, 0) + 1
            if memo[num] > highest:
                highest = memo[num]
        res = [[] for _ in range(highest)] 
        for num in memo.keys():
            count = memo.get(num)
            for i in range(count):
                res[i].append(num)
        return res