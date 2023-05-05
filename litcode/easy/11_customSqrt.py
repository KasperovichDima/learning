class Solution:
    def mySqrt(self, x: int) -> int:
        divider = 2
        res = x // divider

        if res <= 2:
            return int(bool(x)) if not res else res

        while True:
            next_res = res // divider
            next_sqr = next_res * next_res
            next_res_plus_1 = next_res + 1
            if next_sqr > x:
                res //= divider
            elif next_sqr <= x < next_res_plus_1 * next_res_plus_1:
                return int(next_res)
            else:
                divider -= (divider - 1) / 2









s = Solution()

args = (6, 3481, 65165462168, 8, 25, 4, 9, 16, 1, 0, )
results = (2, 59, 255275, 2, 5, 2, 3, 4, 1, 0, )

def test():
    for num, _ in enumerate(args):
        arg = args[num]
        res = results[num]
        assert s.mySqrt(arg) == res
        # print(arg, res)

import time
start = time.perf_counter()
for _ in range(1000):
    test()
print(time.perf_counter() - start)
