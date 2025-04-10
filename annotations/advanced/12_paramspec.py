"""
TODO:

Add type annotations to the class `Wrap`, so that it can be called with the
same arguments as the function it wraps.
"""
from typing import ParamSpec, Callable, Any, Generic, TypeVar


P = ParamSpec('P')
T = TypeVar('T')


class Wrap(Generic[P, T]):
    def __init__(self, func: Callable[P, T]):
        self.func = func

    def __call__(self, *args: P.args, **kwargs: P.kwargs) -> T:
        return self.func(*args, **kwargs)

