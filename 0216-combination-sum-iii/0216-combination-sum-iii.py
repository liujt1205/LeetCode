class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []

        def fill(target, last, cur):
            if target == 0 and len(cur) == k:
                res.append(cur[:])
                return

            if target < 0 or len(cur) == k or last >= target:
                return
            
            for i in range(last + 1, 10):
                cur.append(i)
                fill(target - i, i, cur)
                cur.pop()

        fill(n, 0, [])

        return res