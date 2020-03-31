# This is not really anything to do with types, but works nicely with them.
# https://docs.python.org/3/library/dataclasses.html

from dataclasses import dataclass

@dataclass(frozen=True)
class InventoryItem:
    """Class for keeping track of an item in inventory."""
    name: str
    unit_price: float
    quantity_on_hand: int = 0

    @property
    def total_cost(self) -> float:
        """
        >>> item = InventoryItem(name='rice', unit_price=2.5, quantity_on_hand=3)
        >>> item.total_cost
        7.5
        """
        return self.unit_price * self.quantity_on_hand


# This adds default dunder methods for:
#     init, repr, str, eq, lt, le, gt, ge, hash.
# (Comparison is as if it were a tuple of its fields, in order.)

item1 = InventoryItem(name='toilet paper', unit_price=5)
item2 = InventoryItem(name='lime jam', unit_price=1, quantity_on_hand=100)

print(item1)

# Because frozen, can use as dictionary keys or in a set. (Try removing frozen=True.)
print({item1, item2})
