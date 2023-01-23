#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    list_count = 0
    for element in my_list:
        list_count = list_count + 1
        if count != x:
            try:
                print("{:d}".format(element), end="")
                count = count + 1
            except (TypeError, ValueError):
                continue
        else:
            continue
    if (list_count < x):
        raise IndexError("list index out of range")
    print(end="\n")
    return count
