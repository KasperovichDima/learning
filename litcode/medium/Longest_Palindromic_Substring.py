"""
Given a string s, return the longest
palindromic
substring
in s.

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:

Input: s = "cbbd"
Output: "bb"

Constraints:

    1 <= s.length <= 1000
    s consist of only digits and English letters.
"""

class Solution:

    @staticmethod
    def is_pali(s: str) -> bool:
        return s == s[::-1]

    def longestPalindrome(self, s: str) -> str:
        # if len(s) == 1 or (len(s) == 2 and s[0] == s[1]):
        #     return s

        # result = ''
        left = right = 0

        # while right < len(s):
        chars: set[str] = set()
        left = 0
        for char in s:
            if char in s:
                ...
            chars.add(char)







s = Solution()

cases = (
    'cbbd',  # 'bb'
    'babad',  # 'bab'
    'abba'  # 'abba'
)