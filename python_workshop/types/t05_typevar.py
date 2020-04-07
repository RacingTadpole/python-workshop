import pytest
from decimal import Decimal
from typing import Sequence, TypeVar, List, Union, cast


A = TypeVar("A")  # Can be anything


# Can use to define "generic functions".
# Eg. improve our "get_first" function from before, with the signature:
#     def get_first(values: List[int]) -> int
# Can we generalize this to non-ints? (And non-lists?)

def get_first(seq: Sequence[A]) -> A:
    return seq[0]


def repeat(x: A, n: int) -> List[A]:
    """
    Return a list containing n references to x.
    >>> repeat(7, 3)
    [7, 7, 7]
    >>> repeat('ab', 3)
    ['ab', 'ab', 'ab']
    """
    return [x] * n


# mypy knows the results are different types:
a = repeat(7, 3)
b = repeat('ab', 3)
# Eg. it does not let you combine List[int] and List[str]:
#  print(a + b)  # mypy raises an error (and so does PyCharm)

# although it is valid Python - but its type would be List[Union[int, str]].

# Can work around this using cast.
MyList = List[Union[int, str]]
print(cast(MyList, a) + cast(MyList, b))
