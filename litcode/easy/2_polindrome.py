class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == ''.join(reversed(str(x)))

s = Solution()
print(s.isPalindrome(10))