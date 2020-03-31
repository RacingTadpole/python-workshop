# Based on https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html

from typing import Callable, Iterator


# This is how you annotate a function definition
def stringify(num: int) -> str:
    return str(num)


# Add default value for an argument after the type annotation
def f(num1: int, my_float: float = 3.5) -> float:
    return num1 + my_float


# This is how you annotate a callable (function) value
x: Callable[[int, float], float] = f


# A generator function that yields ints returns an iterator of ints
def g(n: int) -> Iterator[int]:
    i = 0
    while i < n:
        yield i
        i += 1


class Foo:
    def __init__(self, name: str) -> None:
        self.name = name


# Can use class names as types
def fooify(name: str) -> Foo:
    return Foo(name)


foo = fooify('bar')
# reveal_type(foo)  # Revealed type is 'python_workshop.02-functions.Foo'
print(foo.name)

# If you get really stuck, can add:  # type: ignore
