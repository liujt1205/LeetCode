class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        pq = []

        for i in range(len(arr)):
            heapq.heappush(pq, ((arr[i] / arr[-1]), i, len(arr) - 1))

        for _ in range(k - 1):
            cur = heapq.heappop(pq)
            numerator_index = cur[1]
            denominator_index = cur[2] - 1
            if denominator_index > numerator_index:
                heapq.heappush(pq, (
                    (arr[numerator_index] / arr[denominator_index]), 
                    numerator_index, 
                    denominator_index
                ))

        result = heapq.heappop(pq)
        return [arr[result[1]], arr[result[2]]]