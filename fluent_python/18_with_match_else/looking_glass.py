import sys


class LookingGlass:

    def __enter__(self):
        """
        1. Текущий метод sys.stdout.write сохраняется в
           атрибуте экземпляра для последующего использования.
        2. Подменить метод sys.stdout.write своим собственным.
        3. Вернуть строку 'JABBERWOCKY' , просто чтобы было
           что поместить в переменную what .
        """
        self.original_write = sys.stdout.write
        sys.stdout.write = self.reverse_write
        return 'JABBERWOCKY'
    
    def reverse_write(self, text: str) -> None:
        """
        Наш метод sys.stdout.write инвертирует переданный
        аргумент text и вызывает сохраненную реализацию.
        """
        self.original_write(text[::-1])

    # Python вызывает метод __exit__ с аргументами None, None, None,
    # если не было ошибок; если же имело место исключение, то в аргументах
    # передаются данные об исключении, описанные ниже.
    def __exit__(self, exc_type, exc_value, traceback):
        """
        1. Восстановить исходный метод
        2. Если исключение было и его тип – ZeroDivisionError,
           то напечатать сообщение.
        3. и вернуть True , уведомляя интерпретатор что исключение обработано.
        """
        sys.stdout.write = self.original_write  # Восстановить исходный метод
        if exc_type is ZeroDivisionError:
            print('PLease, do not devide by zero))')
            return True
        
    # Если метод __exit__ возвращает None или что-то, похожее на False , то исклю-
    # чение, возникшее внутри блока with , распространяется дальше.


with LookingGlass() as what:
    print('Alice, Kitty and Snowdrop')
    print(what)

print(what)
print('Back to normal.')

# pordwonS dna yttiK ,ecilA
# YKCOWREBBAJ
# JABBERWOCKY
# Back to normal.


# Now let's try to use our glasses without "with":
manager = LookingGlass()
monster = manager.__enter__()
print(monster == 'JABBERWOCKY')
print(manager)
print('What is going on?!!')
manager.__exit__(None, None, None)
print(monster)
print('Uuuuuffff...')

# eurT
# >059965eb06f7x0 ta tcejbo ssalGgnikooL.__niam__<
# !!?no gniog si tahW
# JABBERWOCKY
# Uuuuuffff...

# Now in py 3.10 we can use:
with (
    LookingGlass() as example1,
    LookingGlass() as example2,
    LookingGlass() as example3,
): ...

# instead of:
with LookingGlass() as example1:
    with LookingGlass() as example2:
        with LookingGlass() as example3: ...