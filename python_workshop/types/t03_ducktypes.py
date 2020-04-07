# Based on https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html

from typing import Mapping, Sequence, Iterable, Iterator, Collection

# Actually, don't use List and Tuple unless you really need lists or tuples.

# Instead, use Sequence where a sequence (supporting "len" and "__getitem__")
# is required, eg. don't care if it's a list or tuple.
# mypy ensures Sequences are immutable (no "__setitem__").

# Use Iterable for generic iterables, ie. anything usable in "for"
# (ie. defines "__iter__").


def as_strings(ints: Iterable[int]) -> Sequence[str]:
    return [str(x) for x in ints]  # or tuple, but not set.


result = as_strings(range(1, 3))
# result[1] = 'foo'  # mypy throws an error here, as result is a Sequence, not a List.

print('result: {0}, first: {1}, length: {2}'.format(result, result[0], len(result)))


# Use Mapping for an immutable dict
# Use Collection for a sequence without __getitem__, eg. set. (A collection is Iterable and Sized)

def get_keys(my_mapping: Mapping[int, str]) -> Collection[int]:
    # my_mapping[5] = 'maybe'  # mypy throws an error here, although python would be happy enough.
    return my_mapping.keys()


result2 = get_keys({3: 'yes', 4: 'no'})
print('result: {0}, length: {1}'.format(result2, len(result2)))
# print('first: {0}'.format(result2[0]))  # mypy throws an error. Indeed, python throws TypeError here too.


# A generator function that yields ints returns an iterator of ints
def g(n: int) -> Iterator[int]:
    i = 0
    while i < n:
        yield i
        i += 1


print(list(g(5)))  # returns [0, 1, 2, 3, 4].
