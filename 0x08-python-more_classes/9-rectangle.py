#!/usr/bin/python3
"""This program define a class Rectangle with it attributes"""


class Rectangle:
    """
    A Rectangle Class with the private instance attributes width and height
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        self.instance_tracker(1)
    @classmethod
    def instance_tracker(cls,n):
        cls.number_of_instances += n
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
            rect += str(self.print_symbol) * self.__width
            if i < self.__height -1:
                rect += "\n"
        return rect
    def __repr__(self):
        """ return a string representation of the rectangle"""
        return f"Rectangle({self.__width}, {self.__height})"
    def __del__(self):
        self.instance_tracker(-1)
        print("Bye rectangle...")
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1,Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2,Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        return rect_1 if rect_1.area() >= rect_2.area() else rect_2
    @classmethod
    def square(cls, size=0):
        return cls(size,size)