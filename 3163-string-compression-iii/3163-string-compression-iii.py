class Solution:
    def compressedString(self, word: str) -> str:
        res = ""
        if not word:
            return res
        prev = None
        count = 0
        for char in word:
            if char != prev:
                if count > 0:
                    res = res + str(count) + prev
                prev = char
                count = 1
            else:
                count += 1
                if count > 9:
                    res = res + "9" + prev
                    count -= 9
                
        res = res + str(count) + prev
        return res