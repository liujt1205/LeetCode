class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        res_count = bin(num2).count('1')
        target_count = bin(num1).count('1')
        set_count = 0
        res = 0
        i = 0
        def checkBit(num, index):
            return (num & (1 << index)) != 0

        def setBit(num, index):
            return num | (1 << index)

        while res_count > set_count:
            isSet = checkBit(num1, i)
            if not isSet and target_count < res_count:
                res = setBit(res, i)
                res_count -= 1
            elif isSet and res_count < target_count:
                target_count -= 1
            elif isSet:
                res = setBit(res, i)
                set_count += 1
            i += 1

        return res

