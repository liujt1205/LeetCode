class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        count = {}
        chars = 0
        for char in s1:
            if char not in count:
                count[char] = 0
                chars += 1
            count[char] -= 1
            
        start = 0
        end = 0
        while end < len(s2):
            if s2[end] not in count:
                count[s2[end]] = 0
                chars += 1
            count[s2[end]] += 1
            if count[s2[end]] == 0:
                chars -= 1
                del count[s2[end]]
            if end - start >= len(s1):
                if s2[start] not in count:
                    chars += 1
                    count[s2[start]] = 0
                count[s2[start]] -= 1
                if count[s2[start]] == 0:
                    chars -= 1
                    del count[s2[start]]
                start += 1
            if len(count) == 0:
                return True
            end += 1
        
        return False