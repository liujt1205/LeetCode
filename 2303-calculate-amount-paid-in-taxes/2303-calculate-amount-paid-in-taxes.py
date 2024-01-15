class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        res = 0
        pre = 0
        for i in range(len(brackets)):
            upper, percent = brackets[i]
            if income >= upper:
                res += (upper - pre) * percent / 100
            elif income <= pre:
                break
            else:
                res += (income - pre) * percent / 100
            pre = upper
        return res