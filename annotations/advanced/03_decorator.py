"""
TODO:

Define a decorator that wraps a function and returns a function with the same signature.
The decorator takes an argument `message` of type string
"""
from typing import Callable, TypeVar

T = TypeVar('T', bound=Callable)


def decorator(message: str) -> Callable[[T], T]:
    ...

