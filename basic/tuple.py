from typing import Tuple


def basic_tuple(x: Tuple[str, int]):
    pass


basic_tuple(("foo", 1))
basic_tuple((1, 2)) #type: ignore  #expect-type-error
basic_tuple(("foo", "bar")) #type: ignore  #expect-type-error
basic_tuple((1, "bar")) #type: ignore  #expect-type-error