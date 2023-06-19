def get_count(sentence):
    vowels = ['a', 'e', 'i', 'o', 'u']
    c = 0
    for i in sentence.lower():
        for j in vowels:
            if i == j:
                c += 1
    return c

# def getCount(inputStr):
#     return sum(1 for let in inputStr if let in "aeiouAEIOU")