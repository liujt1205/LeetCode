class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        memo = [set() for _ in range(target + 1)]
        candidates.sort()
        memo[0].add(())
        for i, num in enumerate(candidates):
            for j in range(target - num, -1, -1):
                for tup in memo[j]:
                    memo[j + num].add(tuple(list(tup) + [num]))
                    
        return list(memo[target])