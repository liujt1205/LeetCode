class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        tree = {}
        for region in regions:
            parent = region[0]
            for i in range(1, len(region)):
                tree[region[i]] = parent
        def findPath(region, tree):
            path = []
            path.append(region)
            while region in tree:
                parent = tree[region]
                path.append(parent)
                region = parent
            path.reverse()
            return path
            
        path1 = findPath(region1, tree)
        path2 = findPath(region2, tree)
        
        i, j = 0, 0
        res = ""
        while i < len(path1) and j < len(path2) and path1[i] == path2[j]:
            res = path1[i]
            i += 1
            j += 1
            
        return res