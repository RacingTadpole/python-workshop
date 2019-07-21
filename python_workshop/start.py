from typing import Sequence, TypeVar
import pytest

A = TypeVar('A', int, float)


def sum_sequence(seq: Sequence[A]) -> A:
    """
    Return the sum of the sequence.
    >>> sum_sequence([1, 2, 3, 4])
    10
    >>> sum_sequence((1, 2, 3, 4))
    10
    >>> sum_sequence([1.5, 2, 3])
    6.5
    >>> with pytest.raises(TypeError):
    ...     sum_sequence(['a', 'b', 'c'])
    """
    return sum(seq)
