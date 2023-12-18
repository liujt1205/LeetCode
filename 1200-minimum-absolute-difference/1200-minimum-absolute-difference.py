class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        mindiff = arr[1] - arr[0]
        res = []
        for i in range(1, len(arr)):
            curdiff = arr[i] - arr[i - 1]
            if curdiff < mindiff:
                res.clear()
                res.append([arr[i - 1], arr[i]])
                mindiff = curdiff
            elif curdiff == mindiff:
                res.append([arr[i - 1], arr[i]])
        return res
            