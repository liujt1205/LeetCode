class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        n = len(warehouse)
        room = [0] * n
        left = 0
        right = n - 1
        rightMax = float('inf')
        leftMax = float('inf')
        while left <= right:
            rightMax = min(rightMax, warehouse[right])
            leftMax = min(leftMax, warehouse[left])
            if rightMax > leftMax:
                room[right] = rightMax
                right -= 1
            else:
                room[left] = leftMax
                left += 1
        boxes.sort()
        room.sort()
        res = 0
        boxIndex = len(boxes) - 1
        roomIndex = n - 1
        while roomIndex >= 0 and boxIndex >= 0:
            if room[roomIndex] >= boxes[boxIndex]:
                roomIndex -= 1
                res += 1
            boxIndex -= 1
        return res
            
        