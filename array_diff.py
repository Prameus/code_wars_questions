def array_diff(a, b):
    new_array = []
    for i in a:
        for j in i:
            if j == b[0]:
                i.remove(j)
            else:
                new_array.append(j)
    return list(set(new_array))
print(array_diff(([1,2], [1]), [2]))