print('@ builderlib module start')

class Builder:
    """Это построитель классов"""
    print('@ Builder body')

    def __init_subclass__(cls):
        print(f'@ Builder.__init_subclass__({cls!r})')
        def inner_0(self):
            print(f'@ SuperA.__init_subclass__:inner_0({self!r})')
        cls.method_a = inner_0

    def __init__(self):
        """Определить функцию, добавляемую в подкласс в присваивании ниже."""
        super().__init__()
        print(f'@ Builder.__init__({self!r})')

def deco(cls):
    """Декоратор класса."""
    print(f'@ deco({cls!r})')

    def inner_1(self):
        """Функция, добавляемая в декорированный класс."""
        print(f'@ deco:inner_1({self!r})')

    cls.method_b = inner_1
    # Вернуть класс, полученный в качестве аргумента.
    return cls
    

class Descriptor:
    """Дескрипторный класс"""
    print('@ Descriptor body')

    def __init__(self):
        print(f'@ Descriptor.__init__({self!r})')

    def __set_name__(self, owner, name):
        args = (self, owner, name)
        print(f'@ Descriptor.__set_name__{args!r}')

    def __set__(self, instance, value):
        args = (self, instance, value)
        print(f'@ Descriptor.__set__{args!r}')

    def __repr__(self):
        return '<Descriptor instance>'

print('@ builderlib module end')
