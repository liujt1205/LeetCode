class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        sortedList = sorted(range(len(names)), key=lambda index: -heights[index])
        return [names[i] for i in sortedList]