rom_to_int = dict(
    I=1, V=5, X=10, L=50,
    C=100, D=500, M=1000
)

class Solution:
    def romanToInt(self, s: str) -> int:
        total = ind = 0
        while ind < len(s):
            next_ind = ind + 1 if len(s) - 1 > ind else ind
            match s[ind], s[next_ind]:
                case ('I', 'V' | 'X') | ('X', 'L' | 'C') | ('C', 'D' | 'M'):
                    total += rom_to_int[s[next_ind]] - rom_to_int[s[ind]]
                    ind += 1
                case _:
                    total += rom_to_int[s[ind]]
            ind += 1
        return total

s = Solution()
print(s.romanToInt('III'))
