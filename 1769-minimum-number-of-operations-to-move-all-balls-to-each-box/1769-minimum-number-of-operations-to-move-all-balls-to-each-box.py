class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        res = [0] * n
        count = 0
        for i in range(1, n):
            res[i] = res[i - 1] + int(boxes[i - 1]) + count
            count += int(boxes[i - 1])

        count = 0
        right_move = 0
        for i in range(n - 2, -1, -1):
            res[i] += right_move + int(boxes[i + 1]) + count
            count += int(boxes[i + 1])
            right_move += count

        return res