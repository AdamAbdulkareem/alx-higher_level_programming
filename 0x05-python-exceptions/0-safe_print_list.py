#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for element in my_list:
            if count != x:
                print("{}".format(element), end="")
                count = count + 1
            else:
                continue
        print(end="\n")
    except:
        print("Value error")
    finally:
        return count
