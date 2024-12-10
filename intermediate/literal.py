from typing import Literal


def intermediate_literal(
    direction: Literal[
        "left",
        "right",
    ]
):
    pass


intermediate_literal("left")
intermediate_literal("right")

a = "".join(["l", "e", "f", "t"])
intermediate_literal(a) #type: ignore  #expect-type-error