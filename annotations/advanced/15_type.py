"""
TODO:

`make_object` takes a class returns an instance of it.
"""
from typing import TypeVar

T = TypeVar('T')

def make_object(cls: type[T]) -> T:
    return cls()

