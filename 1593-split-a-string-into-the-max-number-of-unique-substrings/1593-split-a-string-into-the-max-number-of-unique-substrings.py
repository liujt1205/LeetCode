class Solution:    
    def maxUniqueSplit(self, s: str) -> int:
        str_set = set()
        res = [0]
        
        def helper(s, index, str_set):
            if index == len(s):
                res[0] = max(res[0], len(str_set))
                return
            
            for i in range(index, len(s)):
                cur = s[index: i + 1]
                if cur in str_set:
                    continue
                else:
                    str_set.add(cur)
                    helper(s, i + 1, str_set)
                    str_set.remove(cur)
            
        helper(s, 0, str_set)
        return res[0]
            