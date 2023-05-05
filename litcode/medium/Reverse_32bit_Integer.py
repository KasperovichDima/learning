"""
Given a signed 32-bit integer x, return x with its digits reversed.
If reversing x causes the value to go outside the signed 32-bit
integer range [-2^31, 2^31 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers
(signed or unsigned).

-2^31 <= x <= 2^31 - 1

Example 1:

Input: x = 123
Output: 321

Example 2:

Input: x = -123
Output: -321

Example 3:

Input: x = 120
Output: 21

"""
from collections import deque

# class Solution:
#     def reverse(self, x: int) -> int:
#         res: deque[int] = deque()
#         divider = 10
#         rest = 1
#         while rest > 0:
#             rest, result = divmod(x, divider)
#             res.appendleft(result)
#             divider *= 10

#         print(res)

# class Solution:

#     results = []
#     multiplier = 1

#     def reverse(self, x: int) -> int:
#         rest, tmp_res = divmod(x, 10)
#         self.result += tmp_res * self.multiplier
#         if rest > 0:  #
#             self.multiplier *= 10
#             self.reverse(rest)
#         else:  #
#             return self.result

class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        x = -int(s[-1:0:-1]) if x < 0 else int(s[::-1])
        return x if -2_147_483_648 <= x <= 2_147_483_647 else 0




s = Solution()
r = s.reverse(2_247_483_647)
print(r)
