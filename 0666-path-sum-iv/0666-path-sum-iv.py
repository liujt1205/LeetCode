class Solution:
    def pathSum(self, nums: List[int]) -> int:
        pre = [0] * 9
        cur = [0] * 9
        level = 0
        res = 0
        def consolidate():
            nonlocal res, pre, cur
            for i in range(9):
                if cur[i] != -1:
                    cur[i] += pre[(i + 1) // 2]
                elif i % 2 == 1 and cur[i + 1] == -1 and pre[(i + 1) // 2] != -1:
                    res += pre[(i + 1) // 2]
            pre = cur[:]
            cur = [-1] * 9
            
        for i in range(len(nums)):
            curNode = nums[i]
            curLevel, curPos, curVal = curNode // 100, (curNode // 10) % 10, curNode % 10
            if curLevel != level:
                consolidate()
                level = curLevel
            cur[curPos] = curVal
        
        consolidate()
        for i in range(9):
            if pre[i] != -1:
                res += pre[i]
        
        return res