class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        L = len(matchsticks)
        if total % 4 != 0:
            return False
        
        target = total // 4
        memo = {}
        def helper(mask, sides_done):
            cur_total = 0
            for i in range(L - 1, -1, -1):
                if not (mask & (1 << i)):
                    cur_total += matchsticks[L - 1 - i]
                    
            if cur_total > 0 and cur_total % target == 0:
                sides_done += 1
                
            if sides_done == 3:
                return True
            
            if (mask, sides_done) in memo:
                return memo[(mask, sides_done)]
            
            res = False
            
            c = int(cur_total / target)
            rem = target * (c + 1) - cur_total
            for i in range(L - 1, -1, -1):
                if matchsticks[L - 1 - i] <= rem and mask & (1 << i):
                    if helper(mask ^ (1 << i), sides_done):
                        res = True
                        break
            
            memo[(mask, sides_done)] = res
            return res
        
        return helper((1 << L) - 1, 0)