#!/usr/bin/python3
def print_list_integer(my_list=[]):
    for i in my_list:
        if i == len(my_list):
            print("{:d}".format(i), end='')
        else:
            print("{:d}".format(i))
