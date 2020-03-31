# from https://mypy.readthedocs.io/en/stable/more_types.html#newtypes

from typing import NewType

UserId = NewType('UserId', int)


def get_username(user_id: UserId) -> str:
    return f'user{user_id}'


# Mypy will complain about this, because 4606 is an int, not a UserId:

# print(get_username(4606))

print(get_username(UserId(4606)))
