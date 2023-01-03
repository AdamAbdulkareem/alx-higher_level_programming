#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
absolute_number = abs(number)
list_number = int(str(absolute_number)[-1:])
if list_number > 5:
    print("Last digit of {0} is {1} and is greater than 5".format(number, list_number))
elif list_number == 0:
    print("Last digit of {0} is {1} and is 0".format(number, list_number))
else:
    print("Last digit of {0} is {1} and is less than 6 and not 0".format(number, list_number))

