"""Инспектирование класса с декоратором dataclass."""
from dataclasses import InitVar, dataclass, field, fields
from datetime import date
from enum import Enum, auto
from typing import ClassVar, Optional


@dataclass
class DemoDataClass:
    a: int
    b: float = 1.1
    c = 'spam'
    # err: list = []  ValueError: mutable default <class 'list'>
    # for field err is not allowed: use default_factory
    correct: list = field(default_factory=list)



print(DemoDataClass.__annotations__)
# {'a': <class 'int'>, 'b': <class 'float'>}
print(DemoDataClass.__doc__)
# DemoDataClass(a: int, b: float = 1.1)

# print(DemoDataClass.a)
# AttributeError: type object 'DemoDataClass' has no attribute 'a'

dc = DemoDataClass(9)
dc.c = 'whatever'
dc.z = 'secret stash'
# Теперь у экземпляра dc есть атрибут c , но присваивание ему не изменяет
# атрибут класса c . И можно добавить новый атрибут z .

"""
@dataclass принимает несколько именованных аргументов.
@dataclass(*, init=True, repr=True, eq=True, order=False,
unsafe_hash=False, frozen=False)
name    def     for what
init    True    Сгенерировать __init__
repr    True    Сгенерировать __repr__
order   False   Сгенерировать __lt__ , __le__ ,__gt__ , __ge__
unsafe_hash False Сгенерировать__hash__
frozen  False   Делать экземпляры «неизменяемыми»

Если оба аргумента, eq и frozen , равны True , то @dataclass порождает подходя-
щий метод __hash__ , так что экземпляры будут допускать хеширование. В сгене-
рированном методе __hash__ будут использоваться данные из всех полей, кроме
явно исключенных с помощью опции поля, которую мы рассмотрим в разделе
«Опции полей» ниже. Если frozen=False (по умолчанию), то @dataclass установит
атрибут __hash__ равным None , сигнализируя о том, что экземпляры не хешируе-
мые, и тем самым отменив метод __hash__ , унаследованный от суперкласса.
"""

# Постинициализация
"""
Типичные сценарии использования __post_init__ – проверка и вычисление
значений полей на основе других полей.
"""
@dataclass
class HackerClubMember:
    # атрибут класса
    all_handles: ClassVar[set[str]] = set()  
    # если добавить аннотацию set к all_handles , то @dataclass
    # увидит ее и сделает all_handles атрибутом экземпляра.
    # Декоратору @dataclass безразличны типы в аннотациях, за исключением двух
    # случаев. Один из них такой: если тип атрибута равен ClassVar ,
    #  то для него не генерируется поле экземпляра.
    handle: str = ''

    def __post_init__(self):
        cls = self.__class__  # Получить класс экземпляра
        if self.handle == '':
            self.handle = self.name.split()[0]
        if self.handle in cls.all_handles:  # Если self.handle уже присутствует в cls.all_handles
                                            # , возбудить исключение ValueError .
            msg = f'handle {self.handle!r} already exists.'
            raise ValueError(msg)
        cls.all_handles.add(self.handle)


# Инициализируемые переменные, не являющиеся полями
"""
Иногда возникает необходимость передать __init__
аргументы, не являющиеся полями экземпляра.
"""
class DatabaseType:
    def lookup(self, j):
        pass

@dataclass
class C:
    i: int
    j: int | None = None
    database: InitVar[DatabaseType] = None  # init variable
    def __post_init__(self, database):
        if self.j is None and database is not None:
            self.j = database.lookup('j')

my_database = DatabaseType()
c = C(10, database=my_database)

# nitVar не дает декоратору @dataclass обращаться с database как с обычным полем.
# Он не будет создавать для него атрибут экземпляра, а функция dataclasses.fields
# не включит его в список полей.


# Пример использования @dataclass: запись о ресурсе
# из дублинского ядра
class ResourceType(Enum): 
    BOOK = auto()
    EBOOK = auto()
    VIDEO = auto()


@dataclass
class Resource:
    """ Описание мультимедийного ресурса."""
    identifier: str
    title: str = '<untitled>'
    creators: list[str] = field(default_factory=list)
    date: Optional[date] = None
    type: ResourceType = ResourceType.BOOK
    description: str = ''
    language: str = ''
    subjects: list[str] = field(default_factory=list)

    def __repr__(self) -> str:
        cls = self.__class__  # get self class
        cls_name = cls.__name__  # get calss name
        indent = ' ' * 4
        res = [f'{cls_name}(']  # create "Resource("
        for f in fields(cls):  # for each field
            value = getattr(self, f.name)  # get field attr
            res.append(f'{indent}{f.name} = {value!r},')  # add "   field_name = field_value"
        res.append(')')  # close the bracket
        return '\n'.join(res)  # return result joint with \n


description = 'Improving the design of existing code'
book = Resource(
    '978-0-13-475759-9', 'Refactoring, 2 nd Edition',
    ['Martin Fowler', 'Kent Beck'], date(2018, 11, 19),
    ResourceType.BOOK, description, 'EN',
    ['computer programming', 'OOP']
)
print(book)
