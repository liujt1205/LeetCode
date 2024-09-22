class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        
        def generate(start, n, res):
            if start > n:
                return
            res.append(start)
            for next_digit in range(10):
                next_number = start * 10 + next_digit
                if next_number <= n:
                    generate(next_number, n, res)
                else:
                    break
        
        res = []
        for start in range(1, 10):
            generate(start, n, res)
        
        return res