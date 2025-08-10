class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0
        pos = 0
        for i, h in enumerate(heights):
            if stack and h > stack[-1][0]:
                stack.append((h, i))
            elif stack and h == stack[-1][0]:
                continue
            else:
                while stack and stack[-1][0] > h:
                    curMin, pos = stack.pop()
                    curArea = curMin * (i - pos)
                    res = max(res, curArea)

                stack.append((h, pos))
                
        
        while stack:
            curMin, pos = stack.pop()
            curArea = curMin * (len(heights) - pos)
            res = max(res, curArea)

        return res
