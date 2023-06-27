#!/usr/bin/python3
"""This a Square class"""


class Square:
    """Represents a square"""
    
    def __init__(self, size=0):
        """Initializes a square
        Args:
            size (int): size of a side of the square
        Returns: None
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
      
    def area(self):
        return (self.__size**2)
