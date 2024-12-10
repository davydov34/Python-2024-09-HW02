def intermediate_empty_tuple(x: tuple[()]):
    pass


intermediate_empty_tuple(())
intermediate_empty_tuple((1,)) #type: ignore  #expect-type-error