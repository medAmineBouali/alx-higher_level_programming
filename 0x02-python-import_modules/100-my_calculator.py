#!/usr/bin/python3
import sys
if __name__ == "__main__":
    from .calculator_1 import *
a = int(sys.argv[0])
operator = sys.argv[1]
b = int(sys.argv[2])
if sys.argv.__len__ != 3:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    exit(1)
if operator not in {'+','-','*','/'}:
    print("Unknown operator. Available operators: +, -, * and /")
elif operator == '+':
    print("{} {} {} = {}".format(a,operator,b,add(a,b)))
elif operator == '-':
    print("{} {} {} = {}".format(a,operator,b,sub(a,b)))
elif operator == '*':
    print("{} {} {} = {}".format(a,operator,b,mul(a,b)))
elif operator == '/':
    print("{} {} {} = {}".format(a,operator,b,div(a,b)))