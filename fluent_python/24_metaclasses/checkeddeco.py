from collections.abc import Any, Callable
from typing import Any, NoReturn, get_type_hints


class Field:
    def __init__(self, name: str, constructor: Callable) -> None:
        # Для проверки типа во время выполнения используется встроенная функ-
        # ция callable 1 . Проверка на type(None) необходима, потому что Python воспри-
        # нимает None в типе как NoneType , класс None (и потому вызываемый объект),
        # а не как бесполезный конструктор, который только возвращает None.
        if not callable(constructor) or constructor is type(None):
            raise TypeError(f'{name!r} type hint must be callable!')
        self.name = name
        self.constructor = constructor

    def __set__(self, instance: Any, value: Any) -> None:
        """
        Если Checked.__init__ присваивает value значение ...,
        то мы вызываем constructor без аргументов.
        """
        if value is ...:
            value = self.constructor()
        else:
            try:
                # В противном случае вызываем constructor с заданным значением value.
                value = self.constructor(value)
            except (TypeError, ValueError) as e:
                # Если constructor возбуждает одно из этих исключений, то возбуждаем
                # TypeError с содержательным сообщением, в котором указаны имена поля
                # и конструктора, например 'MMIX' is not compatible with year:int.
                type_name = self.constructor.__name__  # smth like 'str' or 'int'
                msg = f'{value!r} is not compatible with {self.name}:{type_name}'
                raise TypeError(msg) from e
        
        instance.__dict__[self.name] = value


def _fields(cls: type) -> dict[str, type]:
    return get_type_hints(cls)


def __init__(self: Any, **kwargs: Any) -> None:
    for name in self._fields():
        value = kwargs.pop(name, ...)
        setattr(self, name, value)
    if kwargs:
        self.__flag_unknown_attrs(*kwargs)


def __setattr__(self: Any, name: str, value: Any) -> None:
    if name in self._fields():
        cls = self.__class__
        descriptor = getattr(cls, name)
        descriptor.__set__(self, value)
    else:
        self.__flag_unknown_attrs(name)


def __flag_unknown_attrs(self: Any, *names: str) -> NoReturn:
    plural = 's' if len(names) > 1 else ''
    extra = ', '.join(f'{name!r}' for name in names)
    cls_name = repr(self.__class__.__name__)
    raise AttributeError(f'{cls_name} has no attribute{plural} {extra}')


def _asdict(self: Any) -> dict[str, Any]:
    return {
        name: getattr(self, name)
        for name, attr in self.__class__.__dict__.items()
        if isinstance(attr, Field) 
    }


def __repr__(self: Any) -> str:
    kwargs = ', '.join(
        f'{key}{value}' for key, value in self._asdict().items()
    )
    return f'{self.__class__.__name__})({kwargs})'

# Напомним, что классы – это экземпляры type . Эти аннотации типов позво-
# ляют предположить, что мы имеем дело с декоратором класса: он прини-
# мает и возвращает класс.
def checked(cls: type) -> type:
    # _fields – функция верхнего уровня, определенная в модуле позднее
    for name, constructor in _fields(cls).items():
        # Замена каждого атрибута, возвращенного _fields , экземпляром дескриптора
        # Field – то, что делал метод __init_subclass__ в примере 24.5. Здесь нам пред-
        # стоит больше работы
        setattr(cls, name, Field(name, constructor))
    # Построить метод класса по _fields и добавить его в декорированный класс.
    cls._fields = classmethod(_fields)  # type: ignore

    instance_methods = (
        __init__,
        __repr__,
        __setattr__,
        _asdict,
        __flag_unknown_attrs,
    )
    # Добавить все элементы instance_methods в cls .
    for method in instance_methods:
        setattr(cls, method.__name__, method)

    return cls