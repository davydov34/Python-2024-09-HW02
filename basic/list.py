from typing import List


def basic_list(x: List[str]):
    pass


basic_list(["foo", "bar"])
basic_list(["foo", 1]) # type: ignore  #expect-type-error