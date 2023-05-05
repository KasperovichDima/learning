"""
Roman numerals are represented by seven different
symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two one's added
together. 12 is written as XII, which is simply X + II. The number 27
is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to
right. However, the numeral for four is not IIII. Instead, the number
four is written as IV. Because the one is before the five we subtract it
making four. The same principle applies to the number nine, which is
written as IX. There are six instances where subtraction is used:

    I can be placed before V (5) and X (10) to make 4 and 9. 
    X can be placed before L (50) and C (100) to make 40 and 90. 
    C can be placed before D (500) and M (1000) to make 400 and 900.

Given an integer, convert it to a roman numeral.

1 <= num <= 3999
"""


class Solution:

    romes = {
        0: 'I II III IV V VI VII VIII IX'.split(),
        1: 'X XX XXX XL L LX LXX LXXX XC'.split(),
        2: 'C CC CCC CD D DC DCC DCCC CM'.split(),
        3: 'M MM MMM'.split()
    }

    def intToRoman(self, num: int) -> str:
        res = ''
        arabians = [int(_) for _ in str(num)]

        for rank, val in enumerate(reversed(arabians)):
            if not val:
                continue
            res = self.romes[rank][val - 1] + res

        return res



s = Solution()
print(s.intToRoman(1506))