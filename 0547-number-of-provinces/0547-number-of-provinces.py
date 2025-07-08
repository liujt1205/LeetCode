class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        res = n
        root = [i for i in range(n)]
        def getRoot(index):
            if root[index] != index:
                root[index] = getRoot(root[index])

            return root[index]

        def union(x, y):
            nonlocal res
            xRoot = getRoot(x)
            yRoot = getRoot(y)
            if xRoot == yRoot:
                return

            if xRoot > yRoot:
                root[xRoot] = yRoot
            else:
                root[yRoot] = xRoot
            res -= 1

        for row in range(n):
            for col in range(row, n):
                if isConnected[row][col] == 1:
                    union(row, col)

        return res
