"""Списковое включение и генераторные выражения"""
import sys
from array import array


"""Построение декартова произведения c помощью спискового включения"""

print('список футболок, доступных в двух цветах и трех размерах')
colors = ['black', 'white']
sizes = list('SML')
t_shirts = [f'Tshirt. Color: {color}, Size: {size}'
            for color in colors for size in sizes]

print(t_shirts)

"""Чтобы расположить элементы сначала по размеру, а затем по цвету, нужно
просто поменять местами предложения for ; после переноса второго предло-
жения for на другую строку стало понятнее, как будет упорядочен результат."""

"""Ниже приведены простые примеры использования генераторных выраже-
ний для построения кортежа и массива."""

symbols = 'lkfngkdjabnmjb'
tuple_example = (tuple(_ for _ in symbols))
print(tuple_example, type(tuple_example), sys.getsizeof(tuple_example))
array_example = array('u', (_ for _ in symbols))
print(array_example, type(array_example), sys.getsizeof(array_example))
