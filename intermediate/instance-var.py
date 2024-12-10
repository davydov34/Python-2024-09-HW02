class intermediate_instance_var:
    bar: int


foo = intermediate_instance_var()
foo.bar = 1

foo.bar = "1" #type: ignore  #expect-type-error