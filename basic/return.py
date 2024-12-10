from typing import assert_type


def basic_return() -> int:
    return 1


assert_type(basic_return(), int)
assert_type(basic_return(), str) #type: ignore  #expect-type-error