from typing import assert_type, TypeVar

from intermediate.generic import intermediate_generic

T = TypeVar('T', bound='int')

def intermediate_generic3(a: T) -> T:
    return a


class MyInt(int):
    pass


assert_type(intermediate_generic3(1), int)
assert_type(intermediate_generic3(MyInt(1)), MyInt)
assert_type(intermediate_generic3("1", str)) #type: ignore  #expect-type-error
intermediate_generic3(["1"], ["2"]) #type: ignore  #expect-type-error
intermediate_generic3("1", 2) #type: ignore  #expect-type-error