class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        n = len(num)
        res = []
        
        def helper(index, last_operand, cur_operand, value, string):
            if index == n:
                if value == target and cur_operand == 0:
                    res.append("".join(string[1:]))
                return
            cur_operand = cur_operand * 10 + int(num[index])
            str_operand = str(cur_operand)
            
            if cur_operand > 0:
                helper(index + 1, last_operand, cur_operand, value, string)
                
            string.append("+")
            string.append(str_operand)
            helper(index + 1, cur_operand, 0, value + cur_operand, string)
            string.pop()
            string.pop()
            if string:
                string.append('-'); string.append(str_operand)
                helper(index + 1, -cur_operand, 0, value - cur_operand, string)
                string.pop();string.pop()

                string.append('*'); string.append(str_operand)
                helper(index + 1, cur_operand * last_operand, 0, value - last_operand + (cur_operand * last_operand), string)
                string.pop();string.pop()
        helper(0, 0, 0, 0, [])    
        return res