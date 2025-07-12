class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) > len(b):
            return self.addBinary(b, a)

        maxLen = len(b)
        res = ""
        carry = 0
        for i in range(maxLen):
            aIndex = len(a) - 1 - i
            bIndex = len(b) - 1 - i
            count = carry
            if b[bIndex] == '1':
                count += 1
            if aIndex >= 0 and a[aIndex] == '1':
                count += 1
            if count == 0:
                res = '0' + res
                carry = 0
            elif count == 1:
                res = '1' + res
                carry = 0
            elif count == 2:
                res = '0' + res
                carry = 1
            else:
                res = '1' + res
                carry = 1

        if carry == 1:
            res = '1' + res

        return res
