class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if len(num1) < len(num2):
            return self.addStrings(num2, num1)
        
        digits1 = list(num1)
        digits2 = list(num2)
        carry = 0
        res = ""
        for i in range(len(digits1)):
            second = 0 if i >= len(digits2) else int(digits2[len(digits2) - i - 1])
            added = second + int(digits1[len(digits1) - 1 - i]) + carry
            if added > 9:
                carry = 1
                added -= 10
            else:
                carry = 0
            res = str(added) + res
            
        if carry:
            res = "1" + res
        
        return res
            