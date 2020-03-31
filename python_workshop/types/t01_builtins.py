# Based on https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html

from decimal import Decimal
from typing import List, Set, Dict, Tuple, Optional, Any, Union


# For simple built-in types, just use the name of the type
i: int = 1
value: float = 1.0
is_ok: bool = True
message: str = "test"
b: bytes = b"test"

# But in practice mypy works types out for us
msg = "hi"
# reveal_type(msg)

# For collections, the name of the type is capitalized, and the
# name of the type inside the collection is in brackets
values: List[int] = [1]
int_set: Set[int] = {6, 7}

# For mappings, we need the types of both keys and values
d: Dict[str, float] = {'field': 2.0}

# For tuples of fixed size, we specify the types of all the elements
t: Tuple[int, str, float] = (3, "yes", 7.5)

# For tuples of variable size, we use one type and ellipsis
t2: Tuple[int, ...] = (1, 2, 3)

# Use Optional[] for values that could be None
s: Optional[str] = 'ok' if is_ok else None

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
# bad_nos: List[NumberType] = [3, 5.5, Decimal('1.2'), complex(1, 0.5), "a"]  # mypy would raise an error

# Use Any if you don't know the type of something or it's too
# dynamic to write a type for
x: Any = None
