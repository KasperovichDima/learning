import re
import reprlib


RE_WORD = re.compile(r'\w+')

class Sentence:

    def __init__(self, text: str) -> None:
        """
        .findall возвращает список всех непересекающихся
        подстрок, соответствующих регулярному выражению.
        """
        self.text = text


    def __repr__(self) -> str:
        """
        Служебная функция reprlib.repr генерирует сокращенные строковые пред-
        ставления структур данных, которые могут быть очень велики. 30 symb by def.
        """
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        for _ in RE_WORD.finditer(self.text):
            yield _.group()


class Sentence_withGenFunc:

    def __init__(self, text: str) -> None:
        self.text = text

    def __repr__(self) -> str:
        """
        Служебная функция reprlib.repr генерирует сокращенные строковые пред-
        ставления структур данных, которые могут быть очень велики. 30 symb by def.
        """
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        return (match.group() for match in RE_WORD.finditer(self.text))