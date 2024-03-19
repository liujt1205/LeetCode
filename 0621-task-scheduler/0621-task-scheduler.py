class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = [0] * 26
        maxCount = 0
        for task in tasks:
            counts[ord(task) - ord('A')] += 1
            maxCount = max(maxCount, counts[ord(task) - ord('A')])
            
        res = (maxCount - 1) * (1 + n)
        
        for count in counts:
            if count == maxCount:
                res += 1
        
        return max(len(tasks), res)