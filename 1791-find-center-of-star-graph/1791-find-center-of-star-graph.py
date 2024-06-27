class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        seen = set()
        for edge in edges:
            for node in edge:
                if node not in seen:
                    seen.add(node)
                else:
                    return node