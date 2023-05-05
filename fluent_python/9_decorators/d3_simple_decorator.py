"""Реализация простого декоратора"""
import time
import functools


def clock(func):
    def clocked(*args):  # arguments for decorated function
        start_time = time.perf_counter()
        result = func(*args)  # some result of decorated function
        elapsed = time.perf_counter() - start_time
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        print(f'[{elapsed:0.8f}s] {name}({arg_str}) -> {result!r}')
        return result  #
    return clocked


@clock
def snooze(seconds):
    time.sleep(seconds)


@clock
def factorial(n):
    return 1 if n < 2 else n*factorial(n-1)


# And now lets update this decorator, using functools.wraps

def upd_clock(func):
    @functools.wraps(func)  # copy __name__ and __doc__ of decorated object.
    def clocked(*args, **kwargs):  # kwarg support added
        t0 = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_lst = [repr(arg) for arg in args]
        arg_lst.extend(f'{k}={v!r}' for k, v in kwargs.items())
        arg_str = ', '.join(arg_lst)
        print(f'[{elapsed:0.8f}s] {name}({arg_str}) -> {result!r}')
        return result
    return clocked

@upd_clock
def upd_snooze(seconds):
    time.sleep(seconds)


@upd_clock
def upd_factorial(n):
    return 1 if n < 2 else n*upd_factorial(n-1)


if __name__ == '__main__':
    print('*' * 40, 'Calling snooze(.123)')
    upd_snooze(.123)
    print('*' * 40, 'Calling factorial(6)')
    print('6! =', upd_factorial(6))