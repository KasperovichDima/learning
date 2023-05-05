"""
Given a string s, find the length of the longest
substring without repeating characters.

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


    0 <= s.length <= 5 * 104
    s consists of English letters, digits, symbols and spaces.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maximum = point = 0
        chars: dict[str, int] = {}
        for ind, char in enumerate(s):
            if char in chars and point <= chars[char]:
                point = chars[char] + 1
            else:
                maximum = max(maximum, ind - point + 1)
            chars[char] = ind

        return maximum

    
s = Solution()

cases = (
    'tmmzuxt',
    'abcdabcde',
    '',
    'oo',
    'pidr1234po123456oo',
)

for case in cases:
    print(s.lengthOfLongestSubstring(case))
