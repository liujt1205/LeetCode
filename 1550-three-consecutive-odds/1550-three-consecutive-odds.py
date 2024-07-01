class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        first = False
        second = False
        for num in arr:
            if num % 2 == 1:
                if second:
                    return True
                elif first:
                    second = True
                else:
                    first = True
            else:
                first = False
                second = False
        return False