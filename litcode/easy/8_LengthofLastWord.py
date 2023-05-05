class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """
        1. strip the string
        2. devide it by spaces
        3. check len of last word

        NOTE: strip is much faster than rstrip.
        """
        return len(s.rstrip().split()[-1])








s = Solution()
args = ('day', 'Hello World', '   fly me   to   the moon  ', 'luffy is still joyboy', 's', 's ', ' s')
# print(s.lengthOfLastWord('s'))
for _ in args:
    print(s.lengthOfLastWord(_))
# 3
# 5
# 4
# 6
# 1
1
# 1
