"""Обобщенные функции с одиночной диспетчеризацией"""
from functools import singledispatch
from collections import abc
import fractions
import decimal
import html
import numbers


# We start fromn:
def htmlize_pre(obj):
    content = html.escape(repr(obj))
    return f'<pre>{content}</pre>'


print(htmlize_pre({'dima': 'poc', 'lesha': 'loh'}))
# <pre>{&#x27;dima&#x27;: &#x27;poc&#x27;, &#x27;lesha&#x27;: &#x27;loh&#x27;}</pre>

# We use singledispatch.
@singledispatch  # 1
def htmlize(obj: object) -> str:
    content = html.escape(repr(obj))
    return f'<pre>{content}</pre>'


@htmlize.register  # 2
def _(text: str) -> str:  # 3
    content = html.escape(text).replace('\n', '<br/>\n')
    return f'<p>{content}</p>'


@htmlize.register  # 4
def _(seq: abc.Sequence) -> str:
    inner = '</li>\n<li>'.join(htmlize(item) for item in seq)
    return '<ul>\n<li>' + inner + '</li>\n</ul>'


@htmlize.register  # 5
def _(n: numbers.Integral) -> str:
    return f'<pre>{n} (0x{n:x})</pre>'


@htmlize.register  # 6
def _(n: bool) -> str:
    return f'<pre>{n}</pre>'


@htmlize.register(fractions.Fraction)  # 7
def _(x) -> str:
    frac = fractions.Fraction(x)
    return f'<pre>{frac.numerator}/{frac.denominator}</pre>'


@htmlize.register(decimal.Decimal)  # 8
@htmlize.register(float)
def _(x) -> str:
    frac = fractions.Fraction(x).limit_denominator()
    return f'<pre>{x} ({frac.numerator}/{frac.denominator})</pre>'


# 1
# @singledispatch помечает базовую функцию, которая обрабатывает тип object.

# 2
# Каждая специализированная функция снабжается декоратором @«base».
# register.

# 3
# Тип первого аргумента, переданного во время выполнения, определяет,
# когда будет использоваться это конкретное определение функции. Имена
# специализированных функций несущественны, и это подчеркнуто выбо-
# ром _ в качестве имени.

# 4
# Для каждого типа, нуждающегося в специальной обработке, регистрирует-
# ся новая функция с подходящей аннотацией типа в первом параметре.

# 5
# Абстрактные базовые классы numbers полезны в сочетании с singledispatch.

# 6
# bool является подтипом numbers.Integral , но singledispatch ищет реализацию
# с самым специфичным подходящим типом независимо от порядка появ-
# ления в программе.

# 7
# Если вы не хотите или не можете добавить аннотации типов в декориро-
# ванную функцию, то можете передать тип декоратору @«base».register . Этот
# синтаксис работает начиная с версии Python 3.4.

# 8
# Декоратор @«base».register возвращает недекорированную функцию, поэто-
# му можно компоновать их, чтобы зарегистрировать два или более типов
# для одной и той же реализации 3.
