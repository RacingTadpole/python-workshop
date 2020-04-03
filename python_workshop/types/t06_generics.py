# From https://mypy.readthedocs.io/en/stable/generics.html
from typing import TypeVar, Generic, List

T = TypeVar('T')


# Just as List, Sequence take a type, so can your classes.

# Eg. Stack[int], Stack[Tuple[int, str]] :

class Stack(Generic[T]):
    def __init__(self) -> None:
        # Create an empty list with items of type T
        self.items: List[T] = []

    def push(self, item: T) -> None:
        self.items.append(item)

    def pop(self) -> T:
        return self.items.pop()

    def empty(self) -> bool:
        return not self.items


stack = Stack[int]()
stack.push(2)
stack.pop()
# stack.push('x')  # mypy would complain about this
