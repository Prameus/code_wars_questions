def disemvowel(string):
    x = ""
    for i in string.lower():
        for j in "aeuio":
            if i==j:
                string.replace("f"," ")
    return string
    # return "".join(x for x in string_ for j in "aeiuo" if x != j )

print(disemvowel("First fixed test"))