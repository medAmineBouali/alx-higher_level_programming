#!/usr/bin/python3
"""This program define a class Rectangle with it attributes"""


class Rectangle:
    """
    A Rectangle Class with the private instance attributes width and height
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """width property getter"""

        return self.__width
    
    @width.setter
    def width(self,value):
        """width property setter"""

        if not isinstance(value,int):
            raise TypeError("width must be an integer")
        if value < 0 :
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height property getter"""
        return self.__height
  
    @height.setter
    def height(self,value):
        """height property setter"""
        if not isinstance(value,int):
            raise TypeError("height must be an integer")
        if value < 0 :
            raise ValueError("height must be >= 0")
        self.__height = value
    def area(self):
        return self.__height * self.__width
    def perimeter(self):
        return self.__height * 2 + self.__width * 2 if self.__height and self.__width else 0
    def __str__(self) -> str:
        """Return the string format of the Rectangle."""
        rect = ""
        if self.__width == 0:
            return rect
        for i in range(0,self.__height):
            rect += "#" * self.__width
            rect += "\n"
        return rect
        