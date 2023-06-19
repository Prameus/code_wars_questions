def pig_it(text):
    text = text.lower()
    the_sentence = list(text.split(" "))
    for i in the_sentence:
        n = i[-1]
        i.replace(f"{n}","")
        i = f"{n}{i}ay"
        return i
print(pig_it("hello world za warudo tokiyo tomere"))