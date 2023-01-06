#!/usr/bin/python3
def max_integer(my_list=[]):
    largest_number = 0
    for number in my_list:
        if largest_number == 0 or largest_number < number:
            largest_number = number
    return largest_number
