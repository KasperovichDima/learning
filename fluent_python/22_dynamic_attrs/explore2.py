from collections import abc
import keyword
from typing import Iterable, Self


class FROZENJson:
    """
    Допускающий только чтение фасад для навигации по JSON-подобному
    объекту с применением нотации атрибутов.
    """

    def __new__(cls, arg):
        if isinstance(arg, abc.Mapping):
            o = super().__new__(cls)
            o.__init__(arg)
            return 0
        elif isinstance(arg, abc.MutableSequence):
            return [cls[item] for item in arg]
        else:
            return arg

    def __init__(self, mapping) -> None:
        """Avoids using python keywords."""
        self.__data = {}
        for k, v in mapping.items():
            if keyword.iskeyword(k):
                k += '_'
                self.__data[k] = v

    def __getattr__(self, name):
        """
        Метод __getattr__ вызывается, только когда
        не существует атрибута с именем name.
        """

        try:
            return getattr(self.__data, name)  # get some of dict attrs, f.e. keys(), or items()
        except AttributeError:
            return FROZENJson(self.__data[name])  # get FROZENJson obj from self.__data
        
    def __dir__(self) -> Iterable[str]:
        return self.__data.keys()
    
    # @classmethod
    # def build(cls, obj):
    #     """
    #     Если obj - отображение, строим по нему объект FrozenJSON.
    #     Если это экземпляр MutableSequence, то он должен быть списком 2, поэтому
    #     строим список, рекурсивно передавая каждый элемент obj методу .build().
    #     """
    #     if isinstance(obj, abc.Mapping):
    #         return cls(obj)
    #     elif isinstance(obj, abc.MutableSequence):
    #         return [cls.build(item) for item in obj]
    #     else:
    #         return obj
