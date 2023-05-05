"""Параметризованные декораторы"""


registry_list = []


def register_simple(func):
    print(f'running register({func})')
    registry_list.append(func)
    return func


@register_simple
def f1():
    print('running f1()')


print('running main()')
f1()
f1()
f1()


registry_set = set()  # 1


def register(active=True):  # 2
    def decorate(func):  # 3
        print('running register'
            f'(active={active})->decorate({func})')
        if active:  # 4
            registry_set.add(func)
        else:
            registry_set.discard(func)  # 5
        return func  # 6
    return decorate  # 7


@register(active=False)  # 8
def fn1():
    print('running f1()')


@register()  # 9
def fn2():
    print('running f2()')


def fn3():
    print('running f3()')


# 1
# Теперь registry имеет тип set , чтобы ускорить добавление и удаление функций.

# 2
# Функция register принимает необязательный именованный аргумент.

# 3
# Собственно декоратором является внутренняя функция decorate , она при-
# нимает в качестве аргумента функцию.

# 4
# Регистрируем func , только если аргумент active (определенный в замыка-
# нии) равен True .

# 5
# Если не active и функция func присутствует в registry , удаляем ее.

# 6
# Поскольку decorate – декоратор, он должен возвращать функцию.

# 7
# Функция register – наша фабрика декораторов, поэтому она возвращает
# decorate .

# 8
# Фабрику @register следует вызывать как функцию, передавая ей нужные па-
# раметры.

# 9
# Даже если параметров нет, register все равно нужно вызывать как функ-
# цию – @register(), – чтобы она вернула настоящий декоратор decorate .


"""
**locals()
Использование **locals() позволяет ссылаться в fmt на любую локальную
переменную funkcii.
"""