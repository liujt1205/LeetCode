"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)
        def helper(row, col, length):
            if length == 1:
                return Node(grid[row][col], True, None, None, None, None)
            
            topLeft = helper(row, col, length // 2)
            topRight = helper(row, col + length // 2, length // 2)
            bottomLeft = helper(row + length // 2, col, length // 2)
            bottomRight = helper(row + length // 2, col + length // 2, length // 2)

            if topLeft.isLeaf and topRight.isLeaf and bottomLeft.isLeaf and bottomRight.isLeaf and topLeft.val == topRight.val == bottomLeft.val == bottomRight.val:
                return Node(topLeft.val, True, None, None, None, None)
            else:
                return Node(1, False, topLeft, topRight, bottomLeft, bottomRight)
            
        return helper(0, 0, n)