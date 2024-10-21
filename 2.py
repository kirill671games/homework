def make_matrix(size, value=0):
    if isinstance(size, int):
        width = height = size
    elif isinstance(size, tuple) and len(size) == 2:
        width, height = size
    else:
        raise ValueError("size должен быть целым числом или кортежем из двух элементов")
    return [[value] * width for _ in range(height)]

result1 = make_matrix(3)
print("[\n     ", ",\n     ".join(str(x) for x in result1), "\n]\n")
result2 = make_matrix((4, 2), 1)
print("[\n     ", ",\n     ".join(str(x) for x in result2), "\n]\n")
