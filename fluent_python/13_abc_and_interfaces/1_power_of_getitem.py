#  Power of __gettem__
class Vowels:
    """Специальный метод __getitem__ - ключ
    к протоколу последовательности."""
    def __getitem__(self, ind: int) -> str:
        return 'AEIOU'[ind]

v = Vowels()

v[0]
'A'
v[-1]
'U'
for c in v:
    print(c)
# A
# E
# I
# O
# U
'E' in v
True
'Z' in v
False
