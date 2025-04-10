"""
TODO:

Define an `Array` type that supports element-wise addition of arrays with identical dimensions and types.
"""
from typing import TypeVarTuple, Generic

Ts = TypeVarTuple("Ts")

class Array(Generic[*Ts]):
    def __add__(self, other: "Array[*Ts]") -> "Array[*Ts]":
        ...

