from typing import assert_type, TypeVar

T = TypeVar('T', int, str)

def intermediate_generic2(a: T, b: T) -> T:
    return a + b


assert_type(intermediate_generic2(1, 2), int)
assert_type(intermediate_generic2("1", "2"), str)
intermediate_generic2(["1"], ["2"]) # type: ignore  #expect-type-error
intermediate_generic2("1", 2) # type: ignore  #expect-type-error