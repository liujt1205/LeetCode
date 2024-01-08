# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        rows, cols = binaryMatrix.dimensions()
        i = 0
        j = cols - 1
        while i < rows and j >= 0:
            if binaryMatrix.get(i, j) == 1:
                j -= 1
            else:
                i += 1
        if j == cols - 1:
            return -1
        else:
            return j + 1