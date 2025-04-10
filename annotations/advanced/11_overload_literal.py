"""
TODO:

foo is a function that returns an integer when second argument is 1, returns a string when second argument is 2, returns a list when second argument is 3, otherwise it returns the first argument.
"""
from typing import Literal, overload, TypeVar, List, Any

T = TypeVar('T')

@overload
def foo(value: T, flag: Literal[1]) -> int:
    ...

@overload
def foo(value: T, flag: Literal[2]) -> str:
    ...

@overload
def foo(value: T, flag: Literal[3]) -> List[Any]:
    ...

@overload
def foo(value: T, flag: Any) -> T:
    ...

def foo(value: T, flag: Any) -> Any:
    ...

