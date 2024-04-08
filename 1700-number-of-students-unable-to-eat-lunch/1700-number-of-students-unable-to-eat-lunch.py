class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        oneCount = 0
        zeroCount = 0
        for i in range(len(students)):
            if students[i] == 1:
                oneCount += 1
            else:
                zeroCount += 1
        for san in sandwiches:
            if san == 0 and zeroCount == 0:
                return oneCount
            if san == 1 and oneCount == 0:
                return zeroCount
            if san == 0:
                zeroCount -= 1
            else:
                oneCount -= 1
        return 0