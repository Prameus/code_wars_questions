def duplicate_encode(word):
    the_array = list(word.lower())
    the_answer = ''
    for i in the_array:
        if (the_array.count(i))> 1:
            the_answer += ")"
        elif (the_array.count(i)) == 1:
            the_answer += "("
    print(the_answer)


# best practice
# def duplicate_encode(word):
#     return "".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])

duplicate_encode("ZtsZMDYQzdaQ@bMRCgNlm!YhCurgfkxV(gdl")
