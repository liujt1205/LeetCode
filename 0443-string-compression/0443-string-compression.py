class Solution:
    def compress(self, chars: List[str]) -> int:
        if not chars:
            return 0
        count = 0
        res = 1
        cur = 0
        for i in range(len(chars)):
            if chars[i] == chars[res - 1]:
                count += 1       
            else:
                if count == 1:
                    chars[res] = chars[i]
                else:
                    strCount = str(count)
                    chars[res:res + len(strCount)] = list(strCount)
                    res += len(strCount)
                    chars[res] = chars[i]
                res += 1
                count = 1
        if count != 1:
            strCount = str(count)
            chars[res:res + len(strCount)] = list(strCount)
            res += len(strCount)
        return res
                    