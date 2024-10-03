class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        biggest = 0
        res = []
        for i in range(len(heights) - 1, -1, -1):
            if heights[i] > biggest:
                res.append(i)
                biggest = heights[i]
                
        res.sort()
        return res