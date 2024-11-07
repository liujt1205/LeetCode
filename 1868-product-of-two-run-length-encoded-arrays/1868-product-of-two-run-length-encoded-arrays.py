class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        res = []
        group1, group2 = -1, -1
        count1, count2 = 0, 0
        while group1 < len(encoded1) - 1 or group2 < len(encoded2) - 1:
            if count1 == 0:
                group1 += 1
                count1 += encoded1[group1][1]
                
            if count2 == 0:
                group2 += 1
                count2 += encoded2[group2][1]
                
            cur = min(count1, count2)
            value = encoded1[group1][0] * encoded2[group2][0]
            if not res or res[-1][0] != value:
                res.append([value, cur])
            else:
                res[-1][1] += cur
            count1 -= cur
            count2 -= cur
            
        return res