#!/usr/bin/python3
def print_list_integer(my_list=[]):
    for i in range(len(my_list)):
        if i == len(my_list) - 1:
            print("{:d}".format(my_list[i]),end='')
        else:
            print("{:d}".format(my_list[i]))
