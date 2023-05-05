# Словари Python иногда используются как записи, в которых ключами явля-
# ются имена полей, а их значения могут иметь разные типы.
# Например, рассмотрим запись, описывающую книгу, в формате JSON или
# на Python:
import json
from typing import TypedDict, TYPE_CHECKING


# book: dict[str, Any] - bad example
# book: dict[str, str | int | list[str]] - bad example

class BookDict(TypedDict):
    """
    TypedDict лишь поддерживает средства проверки 
    типов и полностью игнорируется во время выполнения.

    * напоминающий класс синтаксис для аннотирования словаря типами
      значений каждого «поля»;
    * конструктор, который говорит средству проверки типов, что оно должно
      ожидать словаря с указанными ключами и значениями.
    * «поля» в определении псевдокласса не создают атрибутов экземпляра
    * нельзя написать инициализаторы со значениями по умолчанию для «полей»
    * определения методов не допускаются
    """
    isbn: str
    title: str
    authors: list[str]
    pagecount: int

book: BookDict = {
    "isbn": "0134757599",
    "title": "Refactoring, 2e",
    "authors": ["Martin Fowler", "Kent Beck"],
    "pagecount": 478
}

# Correct usage example:
def demo() -> None:
    book = BookDict(
        isbn='0134757599' ,
        title='Refactoring, 2e' ,
        authors=['Martin Fowler', 'Kent Beck'],
        pagecount=478
    )
    authors = book["authors"]  # Mypy выведет тип authors из аннотации ключа 'authors' в BookDict .

    # Константа typing.TYPE_CHECKING равна True , только когда работает средство про-
    # верки типов. На этапе выполнения она всегда равна False .
    if TYPE_CHECKING:
        # reveal_type – не функция Python, а отладочное средство, предоставляемое
        # Mypy. Именно поэтому она нигде не импортируется.
        reveal_type(authors)
        authors = 'Bob'
        book['weight'] = 4.2
        del book['title']


# TASK: требуется сгенерировать XML-код по записям о книгах, например:
# <BOOK>
#     <ISBN>0134757599</ISBN>
#     <TITLE>Refactoring, 2e</TITLE>
#     <AUTHOR>Martin Fowler</AUTHOR>
#     <AUTHOR>Kent Beck</AUTHOR>
#     <PAGECOUNT>478</PAGECOUNT>
# </BOOK>

AUTHOR_ELEMENT = '<AUTHOR>{}</AUTHOR>'

def to_xml(book: BookDict) -> str:  # GREAT EXAMPLE!
    elements: list[str] = []
    for key, value in book.items():
        if isinstance(value, list):
            elements.extend(
                AUTHOR_ELEMENT.format(n) for n in value  # COOL!
            )
        else:
            tag = key.upper()
            elements.append(f'<{tag}>{value}</{tag}>')
    xml = '\n\t'.join(elements)
    return f'<BOOK>\n\t{xml}\n<\BOOK>'

print(to_xml(book))


# and back process:
def book_from_json(payload: str) -> BookDict:
    return json.loads(payload)