# Based on https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html

from typing import List, Dict


# This is how you annotate a function definition
def stringify(num: int) -> str:
    return str(num)


# Add default value for an argument after the type annotation
def f(num1: int, my_float: float = 3.5) -> float:
    return num1 + my_float


# You could use list...
def triplicate(num: int) -> list:
    return [num, num, num]


# But better to specify types in lists, sets, dicts, eg:
def triplicate2(num: int) -> List[int]:
    return [num] * 3


def get_first(values: List[int]) -> int:
    return values[0]


# Dicts:
def splice(keys: List[str], values: List[int]) -> Dict[str, int]:
    return {k: v for k, v in zip(keys, values)}

# Try changing the return type and running mypy.


# Can use class names as types
class Foo:
    def __init__(self, name: str) -> None:
        self.name = name


def fooify(name: str) -> Foo:
    return Foo(name)


foo = fooify('bar')
# reveal_type(foo)  # Revealed type is 'python_workshop.types.t01_functions.Foo'
print(foo.name)

# If you get really stuck, can ignore typing on a line with:  # type: ignore
