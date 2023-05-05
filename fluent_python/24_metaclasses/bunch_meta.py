# Для создания нового метакласса унаследовать type.
from typing import Any


class MetaBunch(type):
    def __new__(meta_cls, cls_name, bases, cls_dict: dict[str, Any]):
        """
        __new__ работает, как метод класса, но класс является метаклассом, поэто-
        му я назвал первый аргумент meta_cls (часто употребляют также имя mcs ).
        Остальные три аргумента такие же, как в трехаргументной сигнатуре для
        вызова type() с целью непосредственного создания класса.
        """
        # В defaults будет храниться отображение имен
        # атрибутов на их значения по умолчанию
        defaults = {}

        def __init__(self, **kwargs):
            """
            Этот метод будет внедрен в новый класс.

            Прочитать defaults и присвоить соответствующему атрибуту экземпляра
            значение, извлеченное из kwargs или подразумеваемое по умолчанию.
            """
            for name, default in defaults.items():
                setattr(self, name, kwargs.pop(name, default))
            if kwargs:
                # Если в kwargs остались аргументы, значит, не нашлось слотов,
                # в которые их можно было бы поместить.
                extra = ', '.join(kwargs)
                raise AttributeError(f'No slots left for: {extra!r}')
            
        def __repr__(self):
            """__repr__ возвращает строку, которая выглядит как вызов конструктора, на-
            пример Point(x=3) . При этом именованные аргументы, принимающие зна-
            чения по умолчанию, опускаются."""
            rep = ', '.join(f'{name}={value}'
                            for name, default in defaults.items()
                            if (value := getattr(self, name)) != default)
            return f'{cls_name}({rep})'
        
        # Инициализировать пространство имен для нового класса.
        new_dict = dict(__slots__=[], __init__=__init__, __repr__=__repr__)

        # Обойти пространство имен пользовательского класса.
        for name, value in cls_dict.items():
            # Если найдено имя name с двумя подчерками, копировать элемент в про-
            # странство имен нового класса, если его там еще нет.
            if name.startswith('__') and name.endswith('__'):
                if name in new_dict:
                    raise AttributeError(f"Can't set {name} in {cls_name}")
                new_dict[name] = value
            # Если имя атрибута name не начинается двумя подчерками, добавить его
            # в конец __slots__ и сохранить его значение value в defaults.
            else:
                new_dict['__slots__'].append(name)
                defaults[name] = value

        return super().__new__(meta_cls, cls_name, bases, new_dict)


class Bunch(metaclass=MetaBunch):
    """
    Предоставить базовый класс, чтобы пользователи не видели MetaBunch.
    """


class Point(Bunch):
    x = 0.0
    y = 0.0
    color = 'gray'
