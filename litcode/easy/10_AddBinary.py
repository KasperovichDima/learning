# Input: a = "1010", b = "1011"
# Output: "10101"

# Input: a = "11", b = "1"
# Output: "100"


class BestSolution:
    def addBinary(self, a: str, b: str) -> str:
        #  instead of using range (-1 -1 -1) just set first ind -1
        #  and then decrease it on every iteration
        i, rest, result, len_a, len_b = -1, 0, '', -len(a), -len(b)
        while i >= len_a or i >= len_b:  # using indexation
            a_bit = int(a[i]) if i >= len_a else 0  # solving of index problem
            b_bit = int(b[i]) if i >= len_b else 0  # solving of index problem
            sum = a_bit + b_bit + rest
            result = str(sum % 2) + result  # tricky thing
            rest = sum // 2  # tricky thing
            i -= 1

        return '1'+result if rest else result  # using the same add as me


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ''
        transfer = False
        hashed = {'1': True, '0': False, False: '0', True: '1'}
        max_str, min_str = (a, b) if len(a) >= len(b) else (b, a)
        if len(max_str) > len(min_str):
            min_str = min_str.rjust(len(max_str), '0')
        for ind in range(len(max_str) - 1, -1, -1):
            if hashed[max_str[ind]] and hashed[min_str[ind]]:
                res += hashed[transfer]
                if not transfer:
                    transfer = True
            else:
                res += hashed[transfer]\
                    if hashed[max_str[ind]] is hashed[min_str[ind]]\
                    else hashed[not transfer]
                transfer = all((transfer, any((hashed[max_str[ind]],
                                               hashed[min_str[ind]]))))

        if transfer:
            res += '1'
        return res[::-1]


s = Solution()
args = (('111', '1010'), ('1111', '1111'), ('11', '1'), ('1010', '1011'),
        ('0', '0'), ('1', '1'), ('1000', '1'), ('1111', '1'))
for _ in args:
    print(s.addBinary(*_))

111, 1010
10001

1111, 1111
11110

11, 1
100

1010, 1011
10101

0, 0
0

1, 1
10

1000, 1
1001

1111, 1
10000
