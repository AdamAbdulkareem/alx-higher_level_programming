#!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except Exception as te:
        error_type = "Exception: {}"
        print("Exception: {}".format(te.args))
        return False
