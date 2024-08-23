class Solution:
    def fractionAddition(self, expression: str) -> str:
        num = 0
        denom = 1
        
        def findGcd(a, b):
            if a == 0:
                return b
            return findGcd(b % a, a)
            
        i = 0
        while i < len(expression):
            cur_num = 0
            cur_denom = 0
            neg = False
            if expression[i] == "-":
                neg = True
                i += 1
            elif expression[i] == "+":
                i += 1
            while i < len(expression) and expression[i].isdigit():
                val = int(expression[i])
                cur_num = cur_num * 10 + val
                i += 1
            i += 1
            while i < len(expression) and expression[i].isdigit():
                val = int(expression[i])
                cur_denom = cur_denom * 10 + val
                i += 1
            if neg:
                cur_num *= -1
            num = num * cur_denom + cur_num * denom
            denom *= cur_denom
        gcd = abs(findGcd(num, denom))
        num //= gcd
        denom //= gcd
        return f"{num}/{denom}"
    