from typing import TypedDict, NotRequired


class Student(TypedDict):
    name: str
    age: int
    school: NotRequired[str]


a: Student = {"name": "Tom", "age": 15}
b: Student = {"name": "Tom", "age": 15, "school": "Hogwarts"}
c: Student = {"name": 1, "age": 15, "school": "Hogwarts"}  #type: ignore  #expect-type-error
d: Student = {(1,): "Tom", "age": 2, "school": "Hogwarts"}  #type: ignore  #expect-type-error
e: Student = {"name": "Tom", "age": "2", "school": "Hogwarts"}  #type: ignore  #expect-type-error
f: Student = {"z": "Tom", "age": 2} #type: ignore  #expect-type-error

assert Student(name="Tom", age=15) == dict(name="Tom", age=15)
assert Student(name="Tom", age=15, school="Hogwarts") == dict(
    name="Tom", age=15, school="Hogwarts"
)


