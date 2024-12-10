from typing import List

Vector = List[float]


def basic_typealias(v: Vector): ...


basic_typealias([1.1, 2])
basic_typealias(1) #type: ignore  #expect-type-error
basic_typealias(["1"]) #type: ignore  #expect-type-error