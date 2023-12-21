class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        memo = {}
        res = []
        for s in strs:
            key = ''.join(sorted(s))
            new = memo.get(key, [])
            new.append(s)
            memo[key] = new
        for key in memo:
            res.append(memo[key])
        return res