"""От позиционных к чисто именованным параметрам"""


# html generation example:
def tag(name, *content, class_=None, **attrs):
    """Сгенерировать один или несколько HTML-тегов"""
    if class_ is not None:
        attrs['class'] = class_
    attr_pairs = (f' {attr}="{value}"' for attr, value
                  in sorted(attrs.items()))
    attr_str = ''.join(attr_pairs)
    if content:
        elements = (f'<{name}{attr_str}>{c}</{name}>'
                    for c in content)
        return '\n'.join(elements)
    else:
        return f'<{name}{attr_str} />'

print(tag('br'))
# <br />
print(tag('p', 'hello'))
# <p>hello</p>
print(tag('p', 'hello', 'world', class_='sidebar'))
# <p class="sidebar">world</p>

# Если вы вообще не хотите поддерживать позиционные аргументы, оставив тем
# не менее возможность, задавать чисто именованные, включите в сигнатуру
# звездочку * саму по себе:
def f(a, *, b):
    return a, b

print(f(1, b=2))
# (1, 2)
# print(f(1, 2))
# TypeError: f() takes 1 positional argument but 2 were given


"""Чисто позиционные параметры"""

# Чтобы определить функцию, требующую чисто позиционных параметров,
# используйте символ / в списке параметров.
def divmod(a, b, /):
    return (a // b, a % b)

# print(divmod(a=1, b=2))
# TypeError: divmod() got some positional-only arguments passed as keyword arguments: 'a, b'