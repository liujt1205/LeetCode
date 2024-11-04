class Solution:
    def myAtoi(self, s: str) -> int:
        res = 0
        started = False
        sign = 1
        index = 0
        INT_MAX = pow(2, 31) - 1
        INT_MIN = -pow(2, 31)
        while index < len(s) and s[index] == " ":
            index += 1
            
        if index < len(s) and s[index] == "+":
            sign = 1
            index += 1
        elif index < len(s) and s[index] == "-":
            sign = -1
            index += 1
        while index < len(s) and s[index].isdigit():
            digit = int(s[index])
            if res > INT_MAX // 10 or (res == INT_MAX // 10 and digit > INT_MAX % 10):
                return INT_MAX if sign == 1 else INT_MIN
            
            res = res * 10 + digit
            index += 1
            
        return res * sign
                