from typing import TypedDict, Unpack


class Person(TypedDict):
    name: str
    age: int


def foo(**kwargs: Unpack[Person]): ...


person: Person = {"name": "The Meaning of Life", "age": 1983}
foo(**person)
foo(**{"name": "Brian", "age": 20}) # type: ignore


foo(**{"name": "Brian"})  #type: ignore #expect-type-error
person2: dict[str, object] = {"name": "Brian", "age": 20}
foo(**person2)  #type: ignore #expect-type-error
foo(**{"name": "Brian", "age": "1979"})  #type: ignore #expect-type-error