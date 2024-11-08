class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        res = []
        index1 = index2 = index3 = 0
        
        while index1 < len(arr1) and index2 < len(arr2) and index3 < len(arr3):
            if arr1[index1] == arr2[index2] == arr3[index3]:
                res.append(arr1[index1])
                index1 += 1
                index2 += 1
                index3 += 1
            else:
                if arr1[index1] < arr2[index2]:
                    index1 += 1
                elif arr2[index2] < arr3[index3]:
                    index2 += 1
                else:
                    index3 += 1
        
        return res