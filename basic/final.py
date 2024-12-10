from typing import Final

my_list: Final = []

my_list.append(1)
my_list = [] #type: ignore #expect-type-error
my_list = 'something else' #type: ignore  #expect-type-error
