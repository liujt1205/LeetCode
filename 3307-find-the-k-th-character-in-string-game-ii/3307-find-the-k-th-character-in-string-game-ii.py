class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        length = [2 ** i for i in range(len(operations) + 1)]
        res = 0
        while k > 1:
            index = bisect_left(length, k)
            if index <= 0:
                break
            else:
                next_len = length[index - 1]
                k -= next_len
                res += operations[index - 1]
        
        return chr(ord('a') + res % 26)
