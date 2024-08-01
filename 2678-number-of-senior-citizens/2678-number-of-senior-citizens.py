class Solution:
    def countSeniors(self, details: List[str]) -> int:
        res = 0
        for info in details:
            age = int(info[11:13])
            if age > 60:
                res += 1
        return res