#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = x // y
    except ZeroDivisionError:
        print("None")

    finally:
        print("{:d}".format(result))
