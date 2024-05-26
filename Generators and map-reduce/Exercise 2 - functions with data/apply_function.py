def apply_functions(data, *funcs):
    return [[func(item) for item in data] for func in funcs]

data = [1, 2, 3, 4, 5]
multiply_by_two = lambda x: x * 2
add_three = lambda x: x + 3

result = apply_functions(data, multiply_by_two, add_three)
print(result) 