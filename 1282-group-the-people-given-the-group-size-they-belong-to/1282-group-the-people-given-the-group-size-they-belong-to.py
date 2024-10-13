class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        res = []
        open_group = {}
        for i, size in enumerate(groupSizes):
            if size in open_group:
                open_group[size].append(i)
            else:
                open_group[size] = [i]
            if len(open_group[size]) == size:
                res.append(open_group[size])
                del open_group[size]
                
        return res