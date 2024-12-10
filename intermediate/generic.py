from typing import List, assert_type, TypeVar

T = TypeVar('T')

def intermediate_generic(a: T, b: T) -> T: #type: ignore
    return a + b  #type: ignore


assert_type(intermediate_generic(1, 2), int)
assert_type(intermediate_generic("1", "2"), str)
assert_type(intermediate_generic(["1"], ["2"]), List[str])
assert_type(intermediate_generic(1, "2"), int) # type: ignore  #expect-type-error