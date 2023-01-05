#!/usr/bin/python3
import sys
from calculator_1 import *

if __name__ == "__main__":
    if (len(sys.argv) - 1) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>", end="\n")
        sys.exit(1)
    if (
        sys.argv[2] != "+"
        or sys.argv[2] != "-"
        or sys.argv[2] != "*"
        or sys.argv[2] != "/"
    ):
        print("Unknown operator. Available operators: +, -, * and /")
