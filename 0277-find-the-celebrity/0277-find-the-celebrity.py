# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        candidate = 0
        for people in range(1, n):
            if knows(candidate, people):
                candidate = people
                
        for i in range(candidate):
            if knows(candidate, i):
                return -1
            
        for i in range(n):
            if i != n and not knows(i, candidate):
                return -1
            
        return candidate