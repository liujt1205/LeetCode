class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        n = len(word)
        res = []
        for mask in range(1 << n):
            cur = []
            count = 0
            for index in range(n):
                if mask & (1 << index):
                    count += 1
                else:
                    if count > 0:
                        cur.append(str(count))
                        count = 0
                    cur.append(word[index])
            if count > 0:
                cur.append(str(count))
            res.append("".join(cur))
            
        return res