def spining_words(sentence):
    new_sentence = sentence.split()
    new_value = ""
    newest_value = ""
    for i in new_sentence:
        if len(i)>=5: 
            new_value += f"{i[::-1]} "
        else:
            new_value += f"{i} "
    for j,k in enumerate(new_value):
        newest_value += j
    return new_value
    
print(spining_words("Single word"))