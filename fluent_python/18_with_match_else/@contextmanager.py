"""
Декоратор @contextmanager – элегантный и практичный инструмент, объединяю-
щий три разных средства Python: декоратор функции, генератор и предложе-
ние with .
"""
import contextlib
import sys

# В примере 18.5 класс LookingGlass из примера 18.3 заменен генераторной
# функцией.

@contextlib.contextmanager  # Применить декоратор contextmanager .
def looking_glass():
    original_write = sys.stdout.write  # Сохранить исходный метод sys.stdout.write .

    def reverse_write(text):
        """Функция reverse_write сможет вызывать
        original_write потому что та доступна в замыкании."""
        original_write(text[::-1])

    sys.stdout.write = reverse_write  # Заменить sys.stdout.write функцией reverse_write .
    msg = ''  # возможного сообщения об ошибке
    # Отдать значение, которое будет связано с переменной в части as предложе-
    # ния with. В этой точке генератор приостанавливается на время выполнения
    # блока with.
    try:
        yield 'JABBERWOCKY'
    except ZeroDivisionError:
        msg = 'Please DO NOT divide by zero!'
    finally:
        # Когда управление покидает блок with любым способом, выполнение функ-
        # ции возобновляется с места, следующего за yield; в данном случае мы вос-
        # станавливаем исходный метод sys.stdout.write.
        sys.stdout.write = original_write
        if msg:  # Отобразить сообщение об ошибке, если оно не пусто.
            print(msg)


# TESTS:
with looking_glass() as what:
    print('Alice, Kitty and Snowdrop')
    print(what)
print('back to normal')

# pordwonS dna yttiK ,ecilA
# YKCOWREBBAJ
# back to normal


# При наличии декоратора @contextmanager поведение по
# умолчанию изменяется на противоположное: метод __exit__ , предоставляемый
# декоратором, предполагает, что любое исключение, посланное генератору, уже
# обработано и должно быть подавлено.


# Контекстный менеджер looking_glass работает и как декоратор тоже
@looking_glass()
def verse():
    print('The time has come')

verse()
print('back to normal')

# emoc sah emit ehT
# back to normal