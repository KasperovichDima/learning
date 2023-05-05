def cls_name(obj_or_cls):
    cls = type(obj_or_cls)
    if cls is type:
        cls = obj_or_cls
    return cls.__name__.split('.')[-1]


def display(obj):
    cls = type(obj)
    if cls is type:
        return f'<class {obj.__name__}>'
    elif cls in (type(None), int):
        return repr(obj)
    else:
        return f'<{cls_name(obj)} object>'


def print_args(name, *args):
    """
    В этом примере функция print_args
    вызывается из каждого метода дескриптора.
    """
    pseudo_args = ', '.join(display(x) for x in args)
    print(f'-> {cls_name(args[0])}.__{name}__({pseudo_args})')


class Overriding:
    """
    Типичный переопределяющий дескрипторный
    класс с методами __get__ и __set__.
    """

    def __get__(self, instance, owner):
        print_args('get', self, instance, owner)

    def __set__(self, instance, value):
        print_args('set', self, instance, value)


class OverridingNotGet:
    """Переопределяющий дескриптор без метода __get__ ."""

    def __set__(self, instance, value):
        print_args('set', self, instance, value)


class NonOverriding:
    """Здесь нет метода __set__ , т. е. этот дескриптор непереопределяющий."""

    def __get__(self, instance, owner):
        print_args('get', self, instance, owner)


class Managed:
    """Управляемый класс, в котором используется по
    одному экземпляру каждого дескрипторного класса."""

    over = Overriding()
    over_not_get = OverridingNotGet()
    non_over = NonOverriding()

    def spam(self):
        """Метод spam включен для сравнения, потому что методы – также дескрипторы."""

        print(f'-> Managed.spam({display(self)})')


# Создать объект Managed для тестирования.
obj = Managed()
# obj.over активирует метод дескриптора __get__ , передавая ему управляемый
# экземпляр obj во втором аргументе.
obj.over
# # Managed.over активирует метод дескриптора __get__ , передавая ему None во
# # втором аргументе (instance).
# Managed.over
# # Присваивание obj.over активирует метод дескриптора __set__ , передавая
# # ему значение 7 в последнем аргументе.
# obj.over = 7
# # Чтение obj.over по-прежнему активирует метод дескриптора __get__.
# obj.over
# # Установка значения непосредственно в obj.__dict__ в обход дескриптора.
# obj.__dict__['over'] = 8
# # Проверить, что значение попало в obj.__dict__ и ассоциировано с ключом over.
# print(vars(obj))
# # Однако даже при наличии атрибута экземпляра с именем over дескриптор
# # Managed.over все равно переопределяет попытки читать obj.over.
# print(obj.over)
# # Чтение дескриптора через экземпляр вернет сам объект
# # дескриптора, потому что не существует метода __get__
# print(obj.over_not_get)

# obj.non_over
# obj.non_over = 5
# print(obj.non_over)
# del obj.non_over
# obj.non_over
# del obj.non_over
# obj.non_over
print(obj.spam)
obj.spam = 5
print(obj.spam)
del obj.spam
print(obj.spam)

