class Solution:

    def convert(self, s: str, numRows: int) -> str:
        raw_limit = numRows - 1
        raw = 0
        res = ''
        for _ in numRows - 1:
            res += 
            raw = 0 if raw == raw_limit else raw + 1



s = Solution()
cases = (
    ('AB', 1),
    ("PAYPALISHIRING", 3),
    ("PAYPALISHIRING", 4),
    ('A', 6),
    ('CHUPAVENTILYATORELECTRIFICATOR', 2),
    ('PAYPALISHIRING', 2)
)

refs = (
    'AB',
    'PAHNAPLSIIGYIR',
    'PINALSIGYAHRPI',
    'A',
    'CUAETLAOEETIIAOHPVNIYTRLCRFCTR',
    'PYAIHRNAPLSIIG',
)

for num, case in enumerate(cases):
    try:
        assert s.convert(*case) == refs[num]
    except AssertionError:
        print(f'{s.convert(*case)} != {refs[num]}')

print('fIN!')

# print(s.convert("PAYPALISHIRING", 3))  # PAHNAPLSIIGYIR
# print(s.convert("PAYPALISHIRING", 4))  # PINALSIGYAHRPI
