from typing import Callable

SingleStringInput = Callable[[str], None]


def accept_single_string_input(func: SingleStringInput) -> None: ...


def string_name(name: str) -> None: ...


def string_value(value: str) -> None: ...


def int_value(value: int) -> None: ...


def new_name(name: str) -> str: ... #type: ignore # expect-type-error


accept_single_string_input(string_name)
accept_single_string_input(string_value)
accept_single_string_input(int_value) #type: ignore  #expect-type-error
accept_single_string_input(new_name) #type: ignore  #expect-type-error