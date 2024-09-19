class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        res = []
        
        if len(expression) == 0:
            return res
        
        if len(expression) <= 2:
            return [int(expression)]
        
        for i, cur in enumerate(expression):
            if cur.isdigit():
                continue;
                
            left = self.diffWaysToCompute(expression[:i])
            right = self.diffWaysToCompute(expression[i + 1: ])
            
            for left_value in left:
                for right_value in right:
                    if cur == "+":
                        res.append(left_value + right_value)
                    elif cur == "-":
                        res.append(left_value - right_value)
                    elif cur == "*":
                        res.append(left_value * right_value)
            
        return res