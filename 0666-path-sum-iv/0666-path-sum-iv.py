class Solution:
    def pathSum(self, nums: List[int]) -> int:
        pre = [0] * 9
        cur = [-1] * 9
        level = 1
        res = 0
        for i in range(len(nums)):
            curNode = nums[i]
            curLevel, curPos, curVal = curNode // 100, (curNode // 10) % 10, curNode % 10
            if curLevel == level:
                cur[curPos] = curVal
            else:
                for j in range(9):
                    if cur[j] != -1:
                        cur[j] += pre[(j + 1) // 2]
                    elif j % 2 == 1 and cur[j + 1] == -1 and pre[(j + 1) // 2] != -1:
                        res += pre[(j + 1) // 2]
                pre = cur[:]
                cur = [-1] * 9
                level = curLevel
                cur[curPos] = curVal
        for i in range(9):
            if cur[i] != -1:
                cur[i] += pre[(i + 1) // 2]
                res += cur[i]
            elif i % 2 == 1 and cur[i + 1] == -1 and pre[(i + 1) // 2] != -1:
                res += pre[(i + 1) // 2]
        
        return res