class Solution:
    def maximumLength(self, s: str) -> int:
        hash = defaultdict(list)
        
        n = len(s)
        i = 0
        while i < n:
            temp = 1
            ch = s[i]
            while i < n-1 and s[i] == s[i+1]:
                temp += 1
                i += 1
            hash[ch].append(temp)
            i += 1
            
        maxi = -1
        for ch, lis in hash.items():
            lis.sort(reverse=True)
            if lis[0] >= 3:
                maxi = max(maxi, lis[0]-2)
            if len(lis) >= 2:
                if lis[0] >= 2:
                    maxi = max(maxi, min(lis[0]-1, lis[1]))
                if len(lis) >= 3:
                    maxi = max(maxi, lis[2])
                
        return maxi 