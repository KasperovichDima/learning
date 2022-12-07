"""Теория множеств"""


"""
если a и b - множества, то
a | b - их объединение
a & b - пересечение
a - b - разность.
"""
# Подсчет количества вхождений needles в haystack:
# found = len(needles & haystack)

s1 = {1, 2, 3}
s2 = {3, 4, 5}

s1 |= s2
print(s1)

print(s1 | s2)
# {1, 2, 3, 4, 5}
print(s1 & s2)
# {3}
print(s1 - s2)
# {1, 2}
print(s1 ^ s2)
print(s2 ^ s1)
