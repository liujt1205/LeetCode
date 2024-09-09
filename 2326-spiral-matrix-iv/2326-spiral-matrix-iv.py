# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        res = [[-1] * n for _ in range(m)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        def findNext(row, col, i, m, n, res):
            nextRow = row + directions[i][0]
            nextCol = col + directions[i][1]
            if nextRow < 0 or nextRow >= m or nextCol < 0 or nextCol >= n or res[nextRow][nextCol] != -1:
                i = (i + 1) % 4
                nextRow = row + directions[i][0]
                nextCol = col + directions[i][1]
            return (nextRow, nextCol, i)
        
        i = 0
        row, col = 0, 0
        while head:
            res[row][col] = head.val
            row, col, i = findNext(row, col, i, m, n, res)
            head = head.next
            
        return res