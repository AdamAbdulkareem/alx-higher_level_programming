#!/usr/bin/python3
def list_division(my_list_1, my_list_2):
    array_list = []
    result = 0
    for i in range(0, len(my_list_1)):
        for j in range(0, len(my_list_2)):
            result = my_list_1[i] / my_list_2[j]
            array_list.append(result)
            break
        continue
    print("{}".format(array_list))
list_division([14, 12, 10, 8], [7, 6, 5, 4])
