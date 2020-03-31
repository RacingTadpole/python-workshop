# Based on https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html

from typing import Mapping, Sequence, Iterable, Collection


# Use Iterable for generic iterables (anything usable in "for"),
# and Sequence where a sequence (supporting "len" and "__getitem__") is
# required
def as_strings(ints: Iterable[int]) -> Sequence[str]:
    return [str(x) for x in ints]  # or tuple, but not set.


result = as_strings(range(1, 3))
print('result: {0}, first: {1}, length: {2}'.format(result, result[0], len(result)))


# Use Mapping for an immutable dict
# Use Collection for a sequence without __getitem__, eg. set. (A collection is Iterable and Sized)
def get_keys(my_mapping: Mapping[int, str]) -> Collection[int]:
    # my_mapping[5] = 'maybe'  # mypy throws an error here, although python would be happy enough.
    return my_mapping.keys()


result2 = get_keys({3: 'yes', 4: 'no'})
print('result: {0}, length: {1}'.format(result2, len(result2)))
# print('first: {0}'.format(result2[0]))  # mypy throws an error.
