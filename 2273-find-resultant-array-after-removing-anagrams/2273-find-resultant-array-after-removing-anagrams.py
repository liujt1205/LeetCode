class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        pre = ''
        res = []
        for i in range(len(words)):
            sort = ''.join(sorted(words[i]))
            if sort != pre:
                res.append(words[i])
                pre = sort
        return res