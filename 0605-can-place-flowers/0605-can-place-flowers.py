class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        copy = [0] * (len(flowerbed) + 2)
        for i in range(len(flowerbed)):
            copy[i + 1] = flowerbed[i]
        for i in range(1, len(copy) - 1):
            if copy[i] == 0 and copy[i - 1] != 1 and copy[i + 1] != 1:
                copy[i] = 1
                n -= 1
        return n <= 0
            