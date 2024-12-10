class Solution:
    def maximumLength(self, s: str) -> int:
        memo = defaultdict(list)
        n = len(s)
        i = 0
        while i < n:
            count = 1
            while i < n-1 and s[i] == s[i+1]:
                count += 1
                i += 1
            memo[s[i]].append(count)
            i += 1
            
        res = -1
        for value in memo.values():
            value.sort(reverse=True)
            if value[0] >= 3:
                res = max(res, value[0]-2)
            if len(value) >= 2:
                if value[0] >= 2:
                    res = max(res, min(value[0]-1, value[1]))
                if len(value) >= 3:
                    res = max(res, value[2])
                
        return res 