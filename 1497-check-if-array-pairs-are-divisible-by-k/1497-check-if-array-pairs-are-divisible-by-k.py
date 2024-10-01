class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        reminder = [0] * k
        for num in arr:
            reminder[num % k] += 1
        
        print(reminder)
        for i in range(1, k):
            if reminder[i] != reminder[k - i]:
                return False
            
        return reminder[0] % 2 == 0