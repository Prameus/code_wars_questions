def create_phone_number(n):
    new_list = ''.join(str(x) for x in n)
    return f"({new_list[0:3]}) {new_list[3:6]}-{new_list[6::]}"

# def create_phone_number(n):
# 	return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)