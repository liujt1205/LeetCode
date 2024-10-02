class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        count = defaultdict(int)
        for num in arr:
            count[num] += 1
            
        rank = 1
        ranks = {}
        for num in sorted(count.keys()):
            ranks[num] = rank
            rank += 1
            
        res = []
        for num in arr:
            res.append(ranks[num])
            
        return res