class Solution:
    def maxNumberOfAlloys(self, n: int, k: int, budget: int, composition: List[List[int]], stock: List[int], cost: List[int]) -> int:
        start = 0
        end = 1
        while True:
            possible = False
            for mach in composition:
                money = 0
                for i in range(len(mach)):
                    if stock[i] < end * mach[i]:
                        money += (end * mach[i] - stock[i]) * cost[i]
                if money <= budget:
                    start = end
                    end *= 2
                    possible = True
                    break
            if possible == False:
                break
        while start < end:
            target = (start + end) // 2
            possible = False
            for mach in composition:
                money = 0
                for i in range(len(mach)):
                    if stock[i] < target * mach[i]:
                        money += (target * mach[i] - stock[i]) * cost[i]
                if money <= budget:
                    start = target + 1
                    possible = True
                    break
            if possible == False:
                end = target
        return start - 1