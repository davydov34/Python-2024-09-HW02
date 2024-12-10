from typing import Self


class Foo:
    def return_self(self) -> Self:
        return self


class SubclassOfFoo(Foo):
    pass


f: Foo = Foo().return_self()
sf: SubclassOfFoo = SubclassOfFoo.return_self()  #type: ignore #expect-type-error

sf: SubclassOfFoo = Foo.return_self() #type: ignore  #expect-type-error