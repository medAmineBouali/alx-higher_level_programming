#!/usr/bin/python3
"""this is a rectangle class"""


class Rectangle:
    """This defines the properties and methods of rectangles."""

    def __init__(self, width=0, height=0):
            """Initializes the rectangle"""
            self.width = width
            self.height = height

    @property
    def width(self):
        """getter for the private instance attribute width"""
        return (self.__width)
    
    @width.setter
    def width(self, value):
        """setter for the private instance attribute width"""
        if type(value) is not int:
            raise TypeError("Width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value
    
    @property
    def height(self, value):
        """getter for the private instance attribute height"""
        return (self.__height)
    
    @height.setter
    def height(self, value):
        """setter for the private instance attribute height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value