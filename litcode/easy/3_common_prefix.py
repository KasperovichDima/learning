class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix = ''
        for ind, char in enumerate(strs[0]):
            for str_ in strs[1:]:
                if ind == len(str_) or str_[ind] != char:
                    return prefix
            prefix += char
        return prefix

strs = ["flower","flower","flower"]
s = Solution()
print(s.longestCommonPrefix(strs))
