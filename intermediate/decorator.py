from typing import Callable, TypeVar

T = TypeVar("T", bound=Callable)

def intermediate_decorator(func: T) -> T:
    return func


@intermediate_decorator
def foo(a: int, *, b: str) -> None: ...


@intermediate_decorator
def bar(c: int, d: str) -> None: ...


foo(1, b="2")
bar(c=1, d="2")

foo(1, "2") #type: ignore  #expect-type-error
bar(a=1, e="2") #type: ignore  #expect-type-error
intermediate_decorator(1) #type: ignore  #expect-type-error