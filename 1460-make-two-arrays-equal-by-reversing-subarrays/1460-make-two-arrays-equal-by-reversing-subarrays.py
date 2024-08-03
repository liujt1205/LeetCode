class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        count = defaultdict(int)
        for num in target:
            count[num] += 1
        for num in arr:
            count[num] -= 1
            if count[num] < 0:
                return False
        return True