from typing import ClassVar


class intermediate_class_var:
    bar: ClassVar[int]


intermediate_class_var.bar = 1
intermediate_class_var.bar = "1" # type: ignore  #expect-type-error
intermediate_class_var().bar = 1 # type: ignore  #expect-type-error