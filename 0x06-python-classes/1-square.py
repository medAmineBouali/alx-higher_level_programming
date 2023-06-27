#!/usr/bin/python3
"""This a Square class"""


class Square:
    """Represents a square"""

    def __init__(self, size=None):
        """Initializes a square
        Args:
            size : size of a side of the square
        Returns: None
        """
        self.__size = int(size)
