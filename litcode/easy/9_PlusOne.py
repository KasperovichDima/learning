class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        for _ in range(len(digits) - 1, -1, -1):
            if digits[_] != 9:
                digits[_] += 1
                return digits
            else:
                digits[_] = 0
        return [1] + digits



s = Solution()
args = ([1,2,3], [4,3,2,1], [9], [1,9,9,9], [0], [1,1,1], [1,0,0])
# print(s.plusOne([9]))
for _ in args:
    print(s.plusOne(_))

[1,2,4]
[4,3,2,2]
[1,0]
[2,0,0,0]
[1]
[1,1,2]
[1,0,1]