#!/usr/bin/python3
"""This a Square class"""


class Square:

    def __init__(self, size=None):
        if size is not None:
            self.__size = int(size)
