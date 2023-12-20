class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        biggest = arr[n - 1]
        for i in range(n):
            biggest, arr[n - 1 - i] = max(biggest, arr[n - 1 - i]), biggest
            if i == 0:
                arr[n - 1 - i] = -1
        return arr
                
            
                