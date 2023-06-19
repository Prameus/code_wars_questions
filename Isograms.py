def is_isogram(string):
    the_string = list(string.lower())
    for i in the_string:
        if the_string.count(i) >= 2:
            return False
    return True

print(is_isogram("Aba"))

# def is_isogram(string):
# return len(string) == len(set(string.lower()))