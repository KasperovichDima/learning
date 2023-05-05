"""
Пример
Я вырос в Англии, стране, известной своей любовью к чаю. (Лично мне не нра­
вится большинство чаев, которые подают в Англии, но с годами я приобрел вкус к
китайскому и японскому чаям.) Так что моя авторская фантазия придумала про­
грамму для учета распространения чая среди населения. Каждый месяц програм­
ма считывает данные в виде записей наподобие следующей:
"""

from collections import namedtuple
from dataclasses import dataclass


reading_data = namedtuple('reading_data', ('customer, quantity, month, year'))


@dataclass
class Reading:
    customer: str
    quantity: int
    month: int
    year: int

    @property
    def base_charge(self) -> tuple[int, int]:
        return self.base_rate * self.quantity

    @property
    def base_rate(self):
        ...


rd = reading_data('ivan', 10, 5, 2017)
r1 = Reading(*rd)

print(r1.base_charge)
# print(r1.quantity)
# print(r1.month)
# print(r1.year)
