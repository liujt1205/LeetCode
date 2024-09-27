class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        index = 0
        cur = []
        curLen = 0
        while index < len(words):
            if curLen + len(words[index]) + len(cur) <= maxWidth:
                cur.append(words[index])
                curLen += len(words[index])
                index += 1
            else:
                if len(cur) == 1:
                    pad = maxWidth - curLen
                    remainder = 0
                    newLine = cur[0] + " " * pad
                else:
                    pad = (maxWidth - curLen) // (len(cur) - 1)
                    remainder = (maxWidth - curLen) % (len(cur) - 1)
                    newLine = cur[0]
                    for i in range(1, len(cur)):
                        newLine += " " * (pad + (remainder >= i)) + cur[i]
                res.append(newLine)
                cur = []
                curLen = 0
        
        lastLine = ""
        for i in range(len(cur)):
            lastLine += cur[i] + " " * (len(lastLine) + len(cur[i]) < maxWidth)
        lastLine += " " * (maxWidth - len(lastLine))
        res.append(lastLine)
        
        return res