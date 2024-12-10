from typing import Any


def basic_any(value: Any):
    pass


basic_any(1)
basic_any("10")
basic_any(1, 2) #type: ignore #expect-type-error

