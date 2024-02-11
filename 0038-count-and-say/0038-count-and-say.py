class Solution:
    def countAndSay(self, n: int) -> str:
        def count(string):
            pre = 0
            count = 0
            res = []
            for char in string:
                if pre == 0:
                    pre = char
                    count = 1
                elif char != pre:
                    res.append((pre, count))
                    pre = char
                    count = 1
                else:
                    count += 1
            res.append((pre, count))
            return res
        
        def say(arr):
            res = ""
            for num, count in arr:
                res += str(count) + str(num)
            return res
        
        res = "1"
        for i in range(1, n):
            res = say(count(res))
        return res