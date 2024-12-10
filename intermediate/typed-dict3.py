from typing import TypedDict, Required


class Person(TypedDict, total=False):
    name: Required[str]
    age: int
    gender: str
    address: str
    email: str


a: Person = {
    "name": "Capy",
    "age": 1,
    "gender": "Make",
    "address": "earth",
    "email": "capy@bara.com",
}

b: Person = {"name": "Capy"}
c: Person = {"age": 1, "gender": "Male", "address": "", "email": ""}  #type: ignore  #expect-type-error