class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        total = sum(skill)
        target = total // (len(skill) // 2)
        if target * (len(skill) // 2) != total:
            return -1
        
        counter = Counter(skill)
        res = 0
        for num in counter:
            if counter[num] != counter.get(target - num, 0):
                return -1
            res += num * (target - num) * counter[num]
            
        return res // 2