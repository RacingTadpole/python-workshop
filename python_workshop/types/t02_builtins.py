# Based on https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html

from decimal import Decimal
from typing import List, Tuple, Optional, Any, Union, Callable


# No need to declare types of variables internally, usually
msg = "hi"
# reveal_type(msg)

# For tuples of fixed size, we specify the types of all the elements
t: Tuple[int, str, float] = (3, "yes", 7.5)
# reveal_type(t)  # mypy would have figured this out itself

# For tuples of variable size, use ...
t2: Tuple[int, ...] = (1, 2, 3, 4)

# Use Union when something could be one of a few types
l: List[Union[int, str]] = [3, 5, "test", "fun"]

# Use Optional[] for values that could be None - same as Union with None.
s: Optional[str] = "hello"
s = None  # mypy won't complain
# msg = None  # contrast msg, which has type `str`.

# mypy understands a value can't be None in an if-statement
if s is not None:
    print(s.upper())


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


# You can annotate a callable (function)'s arguments and return type with Callable[[],]
def f1(g: Callable[[int, float], float], my_float: float) -> float:
    return g(1, my_float)


print("f1(f, 7.2) = {}".format(f1(f, 7.2)))
