from random import randint

import re
import reprlib


RE_WORD = re.compile(r'\w+')


class SentenceIterator:

    def __init__(self, words) -> None:
        self.words = words
        self.index = 0

    def __next__(self):
        try:
            word = self.words[self.index]  # try to get word of self.words by index
        except IndexError:
            raise StopIteration
        self.index += 1
        return word

    def __iter__(self):
        return self

class Sentence:

    def __init__(self, text: str) -> None:
        """
        .findall возвращает список всех непересекающихся
        подстрок, соответствующих регулярному выражению.
        """
        self.text = text
        self.words = RE_WORD.findall(text)

    def __getitem__(self, index: int) -> str:
        return self.words[index]

    def __len__(self) -> int:
        """Чтобы выполнить требования протокола последовательности"""
        return len(self.words)

    def __repr__(self) -> str:
        """
        Служебная функция reprlib.repr генерирует сокращенные строковые пред-
        ставления структур данных, которые могут быть очень велики. 30 symb by def.
        """
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        # return SentenceIterator(self.words)
        for _ in self.words:
            yield _


s = Sentence('"The time has come," the Walrus said,')
print(s)

for _ in s:
    # Объекты Sentence являются итерируемыми, скоро мы в этом убедимся.
    print(_)

# Будучи итерируемыми, объекты Sentence могут быть использованы для кон-
# струирования списков и других итерируемых типов.
print(list(s))


def d6():
    return randint(1, 6)

# Мы можем вызвать iter() с двумя аргументами, чтобы создать итератор из
# функции или вообще любого вызываемого объекта. В таком случае первый ар-
# гумент должен быть вызываемым объектом, который будет вызываться мно-
# гократно (без аргументов) для порождения значений, а второй – специальным
# маркером (https://en.wikipedia.org/wiki/Sentinel_value): если вызываемый объект
# возвращает такое значение, то итератор не отдает его вызывающей стороне,
# а возбуждает исключение StopIteration.
d6_iter = iter(d6, 1)

for roll in d6_iter:
    print(roll)
# объект d6_iter после исчерпания становится бесполезным.