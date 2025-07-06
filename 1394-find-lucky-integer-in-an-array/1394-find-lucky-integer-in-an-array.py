class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count = defaultdict(int)
        for num in arr:
            count[num] += 1

        res = -1
        for num in count:
            if count[num] == num:
                res = max(res, num)

        return res