class Solution:
    def tribonacci(self, n: int) -> int:
        memo = [-1] * 38
        memo[0] = 0
        memo[1] = 1
        memo[2] = 1
        
        def find(index):
            nonlocal memo
            if memo[index] != -1:
                return memo[index]
            else:
                memo[index] = find(index - 1) + find(index - 2) + find(index - 3)
                return memo[index]
        
        return find(n)
        