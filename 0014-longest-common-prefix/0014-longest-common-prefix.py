class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = list(strs[0])
        end = len(prefix) - 1
        for i in range(1, len(strs)):
            if len(strs[i]) <= end:
                end = len(strs[i]) - 1
            for j in range(end + 1):
                if strs[i][j] != prefix[j]:
                    end = j - 1
                    break
                    
        res = ""
        for i in range(end + 1):
            res = res + prefix[i]
            
        return res
            
        
    