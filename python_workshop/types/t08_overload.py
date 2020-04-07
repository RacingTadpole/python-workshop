from dataclasses import dataclass

from typing import TypeVar, Generic, Sequence, Union, overload

T = TypeVar("T")


@dataclass(frozen=True)
class NamedSequence(Generic[T]):
    """
    You can provide alternative type signatures for a function.
    A good example where you need this is __getitem__, which allows for both x[1] and x[1:3].
    """
    name: str
    values: Sequence[T]

    @overload
    def __getitem__(self, index: int) -> T: ...

    @overload
    def __getitem__(self, index: slice) -> Sequence[T]: ...

    def __getitem__(self, index: Union[int, slice]) -> Union[T, Sequence[T]]:
        """
        >>> x = NamedSequence(name='foo', values=(5, 10, 25, 100))
        >>> x[1]
        10
        >>> x[1:3]
        (10, 25)
        >>> x[1:]
        (10, 25, 100)
        """
        return self.values[index]
