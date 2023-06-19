def number(lines):
    new_array = []
    for k, v in enumerate(lines):
        new_array.append(f"{k+1}:{v}")
    print(new_array)


number(["a", "b", "c"])