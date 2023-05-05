import math
import operator as op
from collections import ChainMap
from itertools import chain
from typing import Any, TypeAlias, NoReturn


Symbol: TypeAlias = str
Atom: TypeAlias = float | int | Symbol
Expression: TypeAlias = Atom | list


def parse(program: str) -> Expression:
    """Читать выражение Scheme из строки."""
    return read_from_tokens(tokenize(program))


def tokenize(s: str) -> list[str]:
    """Преобразовать строку в список лексем."""
    return s.replace('(', ' ( ').replace(')', ' ) ').split()


def read_from_tokens(tokens: list[str]) -> Expression:
    """Читать выражение из последовательности лексем."""


class Environment(ChainMap[Symbol, Any]):
    """ChainMap, позволяющий обновлять элемент на месте."""

    def change(self, key: Symbol, value: Any) -> None:
        """Найти, где определен ключ, и изменить там значение."""
        for map in self.maps:
            if key in map:
                map[key] = value # type: ignore[index]
                return
        raise KeyError
    

def standard_env() -> Environment:
    env = Environment()
    env.update(vars(math))
    env.update(
        {
        '+': op.add,
        '-': op.sub,
        '*': op.mul,
        '/': op.truediv,

        'abs': abs,
        'append': lambda *args: list(chain(*args)),
        'apply': lambda proc, args: proc(*args),
        'begin': lambda *x: x[-1],
        'car': lambda x: x[0],
        'cdr': lambda x: x[1:],

        'number?': lambda x: isinstance(x, (int, float)),
        'procedure?': callable,
        'round': round,
        'symbol?': lambda x: isinstance(x, Symbol),
        }
    )
    return env


def repl(prompt: str = 'lis.py> ') -> NoReturn:
    """Цикл приглашение-чтение-вычисление-печать."""
    global_env = Environment({}, standard_env())
    while True:
        ast = parse(input(prompt))
        val = evaluate(ast, global_env)
        if val is not None:
            print(lispstr(val))

def lispstr(exp: object) -> str:
    """Преобразовать объект Python назад в строку, понятную Lisp."""
    if isinstance(exp, list):
        return '(' + ' '.join(map(lispstr, exp)) + ')'
    else:
        return str(exp)


KEYWORDS = 'quote if lambda define set!'.split()


def evaluate(exp: Expression, env: Environment) -> Any:
    """Вычислить выражение в заданном окружении."""
    match exp:
        case int(x) | float(x):
            return x
        case Symbol(var):
            return env[var]
        case['quote', x]:
            return x
        case ['if', test, consequence, alternative]:
            if evaluate(test, env):
                return evaluate(consequence, env)
            else:
                return evaluate(alternative, env)
        case ['lambda', [*parms], *body] if body:
            return Procedure(parms, body, env)
        case ['define', Symbol(name), value_exp]:
            env[name] = evaluate(value_exp, env)
        case ['define', [Symbol(name), *parms], *body] if body:
            env[name] = Procedure(parms, body, env)
        case ['set!', Symbol(name), value_exp]:
            env.change(name, evaluate(value_exp, env))
        case [func_exp, *args] if func_exp not in KEYWORDS:
            proc = evaluate(func_exp, env)
            values = [evaluate(arg, env) for arg in args]
            return proc(*values)
        case _:
            raise SyntaxError(lispstr(exp))