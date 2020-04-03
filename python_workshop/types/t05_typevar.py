import pytest
from decimal import Decimal
from typing import Sequence, TypeVar, List, Union, cast


A = TypeVar('A')  # Can be anything


# Can use to define "generic functions"
# Eg. improve our "get_first" function from before, which required Sequence[int].

def get_first(seq: Sequence[A]) -> A:
    return seq[0]


def repeat(x: A, n: int) -> List[A]:
    """
    Return a list containing n references to x.
    Note the docstring tests.
    These are run automatically in pytest with the right pytest.ini.
    Unfortunately mypy doesn't type check them.
    >>> repeat(7, 3)
    [7, 7, 7]
    >>> repeat('ab', 3)
    ['ab', 'ab', 'ab']
    """
    return [x] * n


# Mypy does not let you combine List[int] and List[str]
a = repeat(7, 3)
b = repeat('ab', 3)
#  print(a + b)  # mypy raises an error (and so does PyCharm!)

# Although it is valid Python - but its type would be List[Union[int, str]].
# Could work around this using cast.
MyList = List[Union[int, str]]
print(cast(MyList, a) + cast(MyList, b))


# Must be all Decimals or all floats/ints
Number = TypeVar('Number', Decimal, float)

# Actually because Decimal('0.5') + 5 works, we're going to need this version:
BetterNumber = TypeVar('BetterNumber', Union[Decimal, int], float)

# TypeVar if every use must be the same type.
# Union if you can mix the types.


def sum_sequence(seq: Sequence[BetterNumber]) -> BetterNumber:
    """
    Return the sum of the sequence.
    >>> sum_sequence([1, 2, 3, 4])
    10
    >>> sum_sequence([Decimal('1.5'), Decimal('2')])
    Decimal('3.5')
    >>> sum_sequence([2, Decimal('0.5')])  # Can mix int and Decimal
    Decimal('2.5')
    >>> with pytest.raises(TypeError):
    ...     sum_sequence(['a', 'b', 'c'])

    >>> with pytest.raises(TypeError):  # Cannot mix float and Decimal
    ...     sum_sequence([2.5, Decimal('0.5')])
    """
    return sum(seq)
