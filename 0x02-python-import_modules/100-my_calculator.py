#!/usr/bin/python3
import sys
from .calculator_1 import (add,sub,mul,div)
a = int(sys.argv[0])
operator = sys.argv[1]
b = int(sys.argv[2])
if sys.argv.__len__ != 3:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
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