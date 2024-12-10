def basic_kwargs(**kwargs: int | str):
    pass


basic_kwargs(a=1, b="2")
basic_kwargs(a=[1]) #type: ignore  #expect-type-error