from decimal import Decimal
from fractions import Fraction


class ArithmeticProgression:

    def __init__(self, begin, step, end=None) -> None:
        self.begin = begin
        self.step = step
        self.end = end # None -> "бесконечный" ряд

    def __iter__(self):
        res_type = type(self.begin + self.step)  # cool!
        result = res_type(self.begin)  # instantiate res_type using begin val
        forever = self.end is None  # we don't use bool(self.end) because 0 is valid end
        index = 0
        while forever or result < self.end:
            yield result
            index += 1
            result = self.begin + self.step * index  # cool!


# But we can do the same using gen func:

def gen_func(begin, step, end=None):
    result = type(begin + step)(begin)
    forever = end is None
    index = 0
    while forever or result < end:
        yield result
        index += 1
        result = begin + step * index


# Let's take it to the next level!!!

import itertools

gen = itertools.count(1, .5) # will never end((

# С другой стороны, существует функция itertools.takewhile : она порождает ге-
# нератор, который потребляет другой генератор и останавливается, когда за-
# данный предикат станет равен False . Объединив обе функции вместе, мы мо-
# жем написать:
start = 1
end = 3
step = .5
gen = itertools.takewhile(lambda n: n < end, itertools.count(start, step))
print(list(gen)) #  -> [1, 1.5, 2.0, 2.5]

# So we can get:

def aritprog_gen(begin, step, end=None):
    """не является генераторной функцией: в ней нет слова yield.
    Но она возвращает генератор, как и генераторная функция."""
    first = type(begin + step)(begin)
    ap_gen = itertools.count(first, step)
    if end is None:
        return ap_gen
    return itertools.takewhile(lambda n: n < end, ap_gen)
filter