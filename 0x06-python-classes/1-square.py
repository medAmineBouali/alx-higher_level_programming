#!/usr/bin/python3
"""This a Square class"""


class Square:
    __size = None

    def __init__(self, size):
        if size:
            self.__size = int(size)
