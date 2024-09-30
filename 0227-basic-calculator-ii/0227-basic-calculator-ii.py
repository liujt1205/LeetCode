class Solution:
    def calculate(self, s: str) -> int:
        cur_val = 0
        prev_val = 0
        res = 0
        last_sign = '+'
        for i, char in enumerate(s):
            if str.isdigit(char):
                cur_val = cur_val * 10 + int(char)
            if not str.isdigit(char) and char != ' ' or i == len(s) - 1:
                if last_sign == '+' or last_sign == '-':
                    res += prev_val
                    prev_val = cur_val if last_sign == '+' else -cur_val
                elif last_sign == '*':
                    prev_val *= cur_val
                elif last_sign == '/':
                    add = 1 if prev_val % cur_val != 0 and prev_val * cur_val < 0 else 0
                    prev_val = prev_val // cur_val + add
                last_sign = char
                cur_val = 0
                
        res += prev_val
        return res
                
            