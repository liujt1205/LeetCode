class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        order = {}
        for i in range(len(arr2)):
            order[arr2[i]] = i
        newArr = []
        for num in arr1:
            if num in order:
                v = order[num]
            else:
                v = num + len(arr2)
            newArr.append((v, num))
        newArr.sort()
        res = []
        for i, num in newArr:
            res.append(num)
        return res
        
            