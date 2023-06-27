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
        self.size = size
      
    def area(self):
        """area of square
        Returns: square area
        """
        return (self.__size**2)

     @property
    def size(self):
        """Get/set the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
