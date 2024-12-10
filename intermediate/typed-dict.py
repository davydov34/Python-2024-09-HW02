from typing import TypedDict


class Student(TypedDict):
    name: str
    age: int
    school: str


a: Student = {"name": "Tom", "age": 15, "school": "Hogwarts"}
a: Student = {"name": 1, "age": 15, "school": "Hogwarts"} #type: ignore  #expect-type-error
a: Student = {(1,): "Tom", "age": 2, "school": "Hogwarts"} #type: ignore  #expect-type-error
a: Student = {"name": "Tom", "age": "2", "school": "Hogwarts"} #type: ignore  #expect-type-error
a: Student = {"name": "Tom", "age": 2} #type: ignore  #expect-type-error

assert Student(name="Tom", age=15, school="Hogwarts") == dict(
    name="Tom", age=15, school="Hogwarts"
)
