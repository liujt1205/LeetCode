class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        memo = defaultdict(list)
        for string in strings:
            diff = [0]
            for i in range(1, len(string)):
                cur = (ord(string[i]) - ord(string[0]) + 26) % 26
                diff.append(cur)
                
            key = tuple(diff)
            memo[key].append(string)
            
        res = []
        for key in memo:
            res.append(memo[key])
            
        return res