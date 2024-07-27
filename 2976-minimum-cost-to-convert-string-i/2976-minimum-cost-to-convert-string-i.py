class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        min_cost = [[float('inf')] * 26 for _ in range(26)]
        for i in range(26):
            min_cost[i][i] = 0
        for ori, cha, cst in zip(original, changed, cost):
            ori_index = ord(ori) - ord('a')
            cha_index = ord(cha) - ord('a')
            min_cost[ori_index][cha_index] = min(min_cost[ori_index][cha_index], cst)
        
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    min_cost[i][j] = min(min_cost[i][j], min_cost[i][k] + min_cost[k][j])
            
        res = 0
        for i in range(len(source)):
            actual_cost = min_cost[ord(source[i]) - ord('a')][ord(target[i]) - ord('a')]
            if actual_cost == float('inf'):
                return -1
            res += actual_cost
        return res