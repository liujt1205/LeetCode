class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        memo = {}
        for i in range(len(routes)):
            for j in routes[i]:
                memo[j] = memo.get(j, [])
                memo[j].append(i)
        if source == target:
            return 0
        visited = set()
        seen = set()
        buses = deque()
        buses.extend(memo.get(source, []))
        visited.add(source)
        res = 1
        while buses:
            for i in range(len(buses)):
                bus = buses.popleft()
                if bus not in seen:
                    for station in routes[bus]:
                        if station not in visited:
                            buses.extend(memo.get(station, []))
                        if station == target:
                            return res
                    seen.add(bus)
            res += 1
        return -1