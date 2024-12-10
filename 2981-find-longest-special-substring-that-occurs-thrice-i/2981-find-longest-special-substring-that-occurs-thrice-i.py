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
            
        maxi = -1
        for ch, lis in memo.items():
            lis.sort(reverse=True)
            if lis[0] >= 3:
                maxi = max(maxi, lis[0]-2)
            if len(lis) >= 2:
                if lis[0] >= 2:
                    maxi = max(maxi, min(lis[0]-1, lis[1]))
                if len(lis) >= 3:
                    maxi = max(maxi, lis[2])
                
        return maxi 