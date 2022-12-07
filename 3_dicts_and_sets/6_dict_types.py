"""Вариации на тему dict"""
from collections import ChainMap
from collections import Counter
from collections import UserDict
from types import MappingProxyType


# collections.OrderedDict
"""
Поскольку начиная с версии Python 3.6 встроенный словарь dict также хранит
ключи упорядоченными, использовать OrderedDict имеет смысл главным обра-
зом для поддержания обратной совместимости с предыдущими версиями. Тем
не менее в документации приводится несколько оставшихся различий между116
 Словари и множества
dict и OrderedDict.
"""

# collections.ChainMap
"""Хранит список отображений, так что их можно просматривать как единое це-
лое. Поиск производится в каждом отображении в порядке их перечисления
в конструкторе и завершается успешно, если ключ найден хотя бы в одном."""
d1 = dict(a=1, b=3)
d2 = dict(a=2, b=4, c=6)
chain = ChainMap(d1, d2)
print(chain)
print(chain['a'])
print(chain['b'])
print(chain['c'])
"""Экземпляр ChainMap не копирует входные отображения, а хранит ссылки на
них. Все модификации и вставки ChainMap применяются только к первому из
входных отображений."""
chain['c'] = -1
print(d1)

# collections.Counter
"""Отображение, в котором с каждым ключом ассоциирован счетчик. Обновление
существующего ключа увеличивает его счетчик."""
ct = Counter('abracadabra')
print(ct)
# Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}
ct.update('aaaaazzz')
print(ct)
# Counter({'a': 10, 'z': 3, 'b': 2, 'r': 2, 'c': 1, 'd': 1})
print(ct.most_common(3))
# [('a', 10), ('z', 3), ('b', 2)]

# shelve.Shelf
"""
Модуль shelve из стандартной библиотеки предоставляет постоянное хранили-
ще для отображения строковых ключей на объекты Python, сериализованные
в двоичном формате pickle.
"""

# UserDict
"""Рекомендуется создавать новый тип отображения путем расширения клас-
са collections.UserDict , а не dict."""


class StrKeyDict(UserDict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def __contains__(self, key):
        return str(key) in self.data

    def __setitem__(self, key, item):
        self.data[str(key)] = item

# Неизменяемые отображения
"""Модуль types содержит класс-обертку MappingProxyType , который получает ото-
бражение и возвращает объект mappingproxy , допускающий только чтение, но при
этом являющийся динамическим представлением исходного отображения.
Это означает, что любые изменения исходного отображения будут видны и в
mappingproxy , но через него такие изменения сделать нельзя.
"""
d = {1: 'A'}
d_proxy = MappingProxyType(d)
print(d_proxy)
# d_proxy[2] = 'error' will raise an TypeError
# to add another key: value pair we need to add it to original dict
# MappingProxyType is dynamic so no need to create new one.
d[2] = 'error'
print(d_proxy[2])
