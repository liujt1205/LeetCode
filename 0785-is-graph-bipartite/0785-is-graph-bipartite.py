class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        sides = {}
        for i in range(n):
            if i not in sides:
                sides[i] = 0
                stack = [i]
                while stack:
                    cur = stack.pop()
                    for neighbor in graph[cur]:
                        if neighbor not in sides:
                            sides[neighbor] = sides[cur] ^ 1
                            stack.append(neighbor)
                        elif sides[neighbor] == sides[cur]:
                            return False

        return True