# This is not really anything to do with types, but works nicely with them.
# https://docs.python.org/3/library/dataclasses.html

from dataclasses import dataclass


# @dataclass adds default dunder methods for:
#     init, repr, str, eq, lt, le, gt, ge, hash.
# (Comparison is as if it were a tuple of its fields, in order.)

# frozen=True makes it immutable.

@dataclass(frozen=True)
class InventoryItem:
    name: str
    unit_price: float
    quantity_on_hand: int = 0

    @property
    def total_cost(self) -> float:
        """
        Note the docstring tests.
        These are run automatically in pytest, with the right pytest.ini.
        Unfortunately mypy doesn't type check them though :-(

        >>> item = InventoryItem(name='rice', unit_price=2.5, quantity_on_hand=3)
        >>> item.total_cost
        7.5
        >>> InventoryItem(name='beans', unit_price=1.5).quantity_on_hand
        0
        """
        return self.unit_price * self.quantity_on_hand


item1 = InventoryItem(name='toilet paper', unit_price=5)
item2 = InventoryItem(name='lime jam', unit_price=1, quantity_on_hand=100)

print(item1)

# Because frozen, can use as dictionary keys or in a set. (Try removing frozen=True.)
print({item1, item2})
