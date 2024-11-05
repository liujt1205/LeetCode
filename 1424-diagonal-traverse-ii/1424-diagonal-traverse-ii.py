class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        queue = deque([(0, 0)])
        res = []
        while queue:
            row, col = queue.popleft()
            res.append(nums[row][col])
            if row + 1 < len(nums) and col == 0:
                queue.append((row + 1, col))
            if col + 1 < len(nums[row]):
                queue.append((row, col + 1))
                    
        return res