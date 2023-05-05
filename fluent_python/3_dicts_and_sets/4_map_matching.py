"""С опоставление с отображением - образцом."""
from collections import OrderedDict


def get_creators(record: dict) -> list:
    match record:
        case {'type': 'book', 'api': 2, 'authors': [*names]}:
            return names
        case {'type': 'book', 'api': 1, 'author': name}:
            return [name]
        case {'type': 'book'}:
            raise ValueError(f"Invalid 'book' record: {record!r}")
        case {'type': 'movie', 'director': name}:
            return [name]
        case _:
            raise ValueError(f'Invalid record: {record!r}')

# TESTS:
b1 = dict(api=1, author='Douglas Hofstadter',  # noqa: E305
          type='book', title='Gödel, Escher, Bach')
get_creators(b1)
# ['Douglas Hofstadter']
b2 = OrderedDict(api=2, type='book', title='Python in a Nutshell',
                 authors='Martelli Ravenscroft Holden'.split())
get_creators(b2)
# ['Martelli', 'Ravenscroft', 'Holden']
get_creators({'type': 'book', 'pages': 770})
# ValueError: Invalid 'book' record: {'type': 'book', 'pages': 770}
get_creators('Spam, spam, spam')
# ValueError: Invalid record: 'Spam, spam, spam'

"""
Использовать аргумент **extra для сопоставления с лишними парами ключ-
значение необязательно, но если вы хотите собрать их в словарь, то можете ука-
зать одну переменную с префиксом ** .
"""
