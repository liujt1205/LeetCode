class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        left_b = 0
        right_a = 0
        count = [0] * n
        for i in range(n):
            count[i] = left_b
            if s[i] == 'b':
                left_b += 1
                
        for i in range(n - 1, -1, -1):
            count[i] += right_a
            if s[i] == 'a':
                right_a += 1
        
        return min(count)