#!/usr/bin/python3
import sys

if __name__ == "__main__":
    if (len(sys.argv) - 1) == 0:
        print("{} arguments.".format((len(sys.argv) - 1)), end="\n")
    else:
        print("{} arguments:".format((len(sys.argv) - 1)), end="\n")
        for i in range(1, len(sys.argv)):
            print("{}: {}".format(i, sys.argv[i]))
