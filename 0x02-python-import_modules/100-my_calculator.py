#!/usr/bin//python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
import sys
if len(sys.argv) - 1 != 3:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
exit(1)
a = int(sys.argv[1])
b = int(sys.argv[3])
operator = int(sys.argv[2])
if operator == "+":
    print("{} {} {} ={}".format(a, operator, b, add(a, b)))
elif operator == "-":
    print("{} {} {} ={}".format(a, operator, b, sub(a, b)))
elif operator == "*":
    print("{} {} {} ={}".format(a, operator, b, mul(a, b)))
elif operator == "/":
    print("{} {} {} ={}".format(a, operator, b, div(a, b)))
else:
    print("Unknown operator. Available operators: +, -, * and /")
exit(1)
