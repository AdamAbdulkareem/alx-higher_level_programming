#!/usr/bin/python3
def no_c(my_string):
    stringfy_list = list(my_string)
    for i in range(0, (len(stringfy_list) - 2)):
        if stringfy_list[i] == "c" or stringfy_list[i] == "C":
            stringfy_list.pop(i)
        else:
            continue
    return "".join(stringfy_list)
