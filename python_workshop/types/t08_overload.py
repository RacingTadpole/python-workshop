from dataclasses import dataclass

from typing import TypeVar, Generic, Sequence, Union, overload

T = TypeVar('T')


@dataclass(frozen=True)
class NamedSequence(Generic[T]):
    name: str
    values: Sequence[T]

    @overload
    def __getitem__(self, index: int) -> T: ...

    @overload
    def __getitem__(self, index: slice) -> Sequence[T]: ...

    def __getitem__(self, index: Union[int, slice]) -> Union[T, Sequence[T]]:
        """
        >>> s = NamedSequence(name='foo', values=(5, 10, 25, 100))
        >>> s[2]
        25
        >>> s[2:]
        (25, 100)
        """
        return self.values[index]
