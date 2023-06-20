def get_middle(s):
    if len(s)% 2 == 0:
        return "".join((s[int((len(s)-1)/2)],s[int((len(s)+1)/2)]))
    else:
        return s[int((len(s)-1)/2)]
print(get_middle("testings"))

# def get_middle(s):
#     index, odd = divmod(len(s), 2)
#     return s[index] if odd else s[index - 1:index + 1