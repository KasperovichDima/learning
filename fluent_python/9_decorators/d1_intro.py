"""Краткое введение в декораторы"""

# def deco(func):
#     def inner():
#         print('running inner()')
#     return inner  # deco возвращает свой внутренний объект-функцию inner

# @deco
# def target():  # target декорирована deco
#     print('running target()')

# target()  # При вызове декорированной функции target
# на самом деле выполняется inner
# running inner()
# print(target)  # target теперь ссылается на inner
# <function deco.<locals>.inner at 0x7f8438adc5e0>

"""
Следующие три факта – главное, что нужно знать о декораторах:
 декоратор – это функция или другой вызываемый объект;
 декоратор может заменить декорируемую функцию другой;
 декораторы выполняются сразу после загрузки модуля.
"""

# В registry хранятся ссылки на функции, декорированные @register
registry = []

# register принимает функцию в качестве аргумента
def register(func):
    # Показать, какая функция декорируется, – для демонстрации
    print(f'running register({func})')
    # Включить func в registry
    registry.append(func)
    # Вернуть func : мы должны вернуть функцию, в данном случае возвращается
    # та же функция, что была передана на входе
    return func

@register
def f1():
    print('running f1()')

@register
def f2():
    print('running f2()')

def f3():
    print('running f3()')

def main():
    print('running main()')
    print('registry ->', registry)
    f1()
    f2()
    f3()


if __name__ == '__main__':
    main()
# running register(<function f1 at 0x7f2236e88900>)
# running register(<function f2 at 0x7f2236e885e0>)
# running main()
# registry -> [<function f1 at 0x7f2236e88900>, <function f2 at 0x7f2236e885e0>]
# running f1()
# running f2()
# running f3()