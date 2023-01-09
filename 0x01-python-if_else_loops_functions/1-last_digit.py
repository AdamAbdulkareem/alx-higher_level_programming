#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
last_number = number % 10

if number < 0:
    absolute_number = abs(number)
    negative_last_number = last_number * -1
    if negative_last_number > 5:
        print(
            "Last digit of {0} is {1} and is greater than 5".format(
                number, negative_last_number
            )
        )
    elif negative_last_number == 0:
        print("Last digit of {0} is {1} and is 0".format(number, negative_last_number))
    else:
        print(
            "Last digit of {0} is {1} and is less than 6 and not 0".format(
                number, negative_last_number
            )
        )

else:
    if last_number > 5:
        print(
            "Last digit of {0} is {1} and is greater than 5".format(number, last_number)
        )
    elif last_number == 0:
        print("Last digit of {0} is {1} and is 0".format(number, last_number))
    else:
        print(
            "Last digit of {0} is {1} and is less than 6 and not 0".format(
                number, last_number
            )
        )
