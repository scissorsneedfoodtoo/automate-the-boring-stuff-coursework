my_list = ['apples', 'bananas', 'tofu', 'cats']

def listifier(user_list):
    output = ""
    for index, entry in enumerate(user_list):
        final_index = len(user_list) - 1
        if index < final_index:
            output += entry + ", "
        else:
            output += "and " + entry
    return output

print(listifier(my_list))
