from collections.abc import Callable
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


class Checked:
    @classmethod
    def _fields(cls) -> dict[str, type]:
        return get_type_hints(cls)
    
    def __init_subclass__(cls) -> None:
        """__init_subclass__ вызывается, когда определяется подкласс текущего класса."""
        super().__init_subclass__()
        for name, constructor in cls._fields().items():
            setattr(cls, name, Field(name, constructor))

    def __init__(self, **kwargs: Any) -> None:
        for name in self._fields():  #Для каждого поля класса name …
            # … получить соответствующее значение value из kwargs и удалить его из kwargs.
            # Использование ... (объект Ellipsis) в качестве значения по умолчанию по-
            # зволяет отличить заданные аргументы со значением None от незаданных
            value = kwargs.pop(name)
            # Этот вызов setattr вызывает срабатывание метода
            # Checked.__setattr__ , показанного в примере 24.6.
            setattr(self, name, value)
        if kwargs:
            # Если в kwargs остались аргументы, то их имена не совпадают
            # ни с одним из объявленных полей, и __init__ завершается ошибкой.

            # Об этой ошибке сообщает метод __flag_unknown_attrs , показанный в
            # примере 24.6. Он принимает аргумент *names , содержащий имена неизвестных
            # атрибутов. Я использовал в *kwargs одну звездочку, чтобы передать ключи
            # в виде последовательности аргументов.
            self.__flag_unknown_attrs(*kwargs)

    def __setattr__(self, __name: str, __value: Any) -> None:
        """
        Перехватывать все попытки установить атрибут экземпляра. Необходимо,
        чтобы предотвратить присваивание неизвестному атрибуту.
        """
        if __name in self._fields():
            # Если атрибут с именем name известен, получить соответствующий дескриптор.
            cls = self.__class__
            descriptor = getattr(cls, __name)
            descriptor.__set__(self, __value)
            # Обычно нам нет нужды вызывать метод __set__ дескриптора явно. Но в дан-
            # ном случае это необходимо, потому что __setattr__ перехватывает все по-
            # пытки установить атрибут экземпляра, даже при наличии переопределяю-
            # щего дескриптора типа Field.
        else:
            # В противном случае атрибут с именем name неизвестен,
            # и метод __flag_unknown_attrs возбуждает исключение.
            self.__flag_unknown_attrs(__name)

    def __flag_unknown_attrs(self, *names: str) -> NoReturn:
        """Сконструировать полезное сообщение об ошибке, содержащее все неожи-
            данные аргументы, и возбудить исключение AttributeError . Это редкий при-
            мер специального типа NoReturn , рассмотренного в одноименном разделе
            главы 8."""

        plural = 's' if len(names) > 1 else ''
        extra = ', '.join(f'{name!r}' for name in names)
        cls_name = repr(self.__class__.__name__)
        raise AttributeError(f'{cls_name} object has no attribute{plural} {extra}')
    
    def _asdict(self) -> dict[str, Any]:
        return {
            name: getattr(self, name)
            for name, attr in self.__class__.__dict__.items()
            if isinstance(attr, Field)
        }
    
    def __repr__(self) -> str:
        """Желание реализовать полезное представление в методе __repr__ - основная
        причина наличия метода _asdict в этом примере."""
        kwargs = ', '.join(
            f'{key}={value}' for key, value in {self._asdict().items()}
        )
        return f'{self.__class__.__name__}({kwargs})'