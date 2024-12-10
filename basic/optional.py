from typing import Optional


def basic_optional(x: Optional[int] = None):
    pass


basic_optional(10)
basic_optional(None)
basic_optional()

foo("10") # type: ignore  #expect-type-error
