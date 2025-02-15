class Solution:
    def punishmentNumber(self, n: int) -> int:
        def can_partition(num, target):
            if target < 0 or num < target:
                return False

            if num == target:
                return True

            return (can_partition(num // 10, target - num % 10)
                or can_partition(num // 100, target - num % 100)
                or can_partition(num // 1000, target - num % 1000))

        res = 0
        for i in range(1, n + 1):
            square = i * i
            if can_partition(square, i):
                res += square

        return res 