class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        res = 1
        not_even = bool(n%2)
        min_el_num = n//2+1 if not_even else n//2
        for _ in range(min_el_num+1, n):
            res += _
        return res + min_el_num if not_even else res + 1


args = 1,6,3,2,4,5
results = 1,13,3,2,5,8

s=Solution()
def test():
    for _ in range(len(args)):
        print(args[_])
        print(results[_])
        # s.climbStairs(args[_])
        assert s.climbStairs(args[_]) == results[_]

test()
