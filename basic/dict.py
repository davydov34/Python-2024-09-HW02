from typing import Dict


def basic_dict(x: Dict[str, str]):
    pass


basic_dict({"foo": "bar"})
basic_dict({"foo": 1}) #type: ignore #expect-type-error
