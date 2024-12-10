from typing import Union


def basic_union(x: Union[int, str]):
    pass


basic_union("foo")
basic_union(1)
basic_union([]) #type: ignore  #expect-type-error