class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        child = defaultdict(set)
        degree = [0] * numCourses
        
        for a, b in prerequisites:
            child[b].add(a)
            degree[a] += 1
            
        queue = deque()
        count = 0
        for i in range(numCourses):
            if degree[i] == 0:
                queue.append(i)
                
        while queue:
            cur = queue.popleft()
            count += 1
            for cour in child[cur]:
                degree[cour] -= 1
                if degree[cour] == 0:
                    queue.append(cour)
                    
        return count == numCourses