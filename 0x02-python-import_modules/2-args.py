#!/usr/bin/python3
import sys

num_arguments = len(sys.argv) - 1
array_arguments = sys.argv
if __name__ == "__main__":
    if num_arguments == 0:
        print("{} arguments.".format(num_arguments), end="\n")
    else:
        print("{} arguments:".format(num_arguments), end="\n")
        for i in range(1, num_arguments + 1):
            print("{}: {}".format(i, array_arguments[i]))
