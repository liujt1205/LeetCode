class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        res = 0
        pre = 0
        for row in bank:
            count = 0
            for char in row:
                if char == '1':
                    count += 1
            if count != 0:
                res += count * pre
                pre = count
        return res