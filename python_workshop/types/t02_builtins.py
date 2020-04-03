# Based on https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html

from decimal import Decimal
from typing import List, Tuple, Optional, Any, Union, Callable


# No need to declare types of variables internally, usually
msg = "hi"
# reveal_type(msg)

# For tuples of fixed size, we specify the types of all the elements
t: Tuple[int, str, float] = (3, "yes", 7.5)

# For tuples of variable size, we use one type and ellipsis
t2: Tuple[int, ...] = (1, 2, 3)

# Use Optional[] for values that could be None
s: Optional[str]

# Mypy understands a value can't be None in an if-statement
if s is not None:
    print(s.upper())

# If a value can never be None due to some invariants, use an assert
assert s is not None
print(s.upper())

# Use Union when something could be one of a few types
l: List[Union[int, str]] = [3, 5, "test", "fun"]

# Can also define type aliases using =.
# Note this is equivalent to the target type, not a new type.
NumberType = Union[Decimal, complex]  # complex includes float, and float includes int
nos: List[NumberType] = [3, 5.5, Decimal('1.2'), complex(1, 0.5)]

# not_nos: List[NumberType] = [3, 5.5, Decimal('1.2'), complex(1, 0.5), "a"]  # mypy would raise an error

# Use Any if you don't know the type of something or it's too
# dynamic to write a type for
x: Any = None


def f(num1: int, my_float: float) -> float:
    return num1 + my_float


# This is how you annotate a callable (function) value
g: Callable[[int, float], float] = f
