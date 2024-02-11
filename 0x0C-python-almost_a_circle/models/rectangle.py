#!/usr/bin/python3
"""Defines a rectangle class."""
from models.base import Base

class Rectangle(Base):
    """Represent a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): The x-coordinate of the rectangle's position.
            y (int): The y-coordinate of the rectangle's position.
            id (int): The identifier of the rectangle.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, val):
        """
        Set the width of the rectangle.

        Args:
            val (int): The new width value.
        """
        if not type(val) is int:
            raise TypeError("width must be an integer")
        if val >= 0:
            self.__width = val
        else:
            self.__width = 0
            raise ValueError("width must be > 0")

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, val):
        """
        Set the height of the rectangle.

        Args:
            val (int): The new height value.
        """
        if not type(val) is int:
            raise TypeError("height must be an integer")
        if val >= 0:
            self.__height = val
        else:
            self.__height = 0
            raise ValueError("height must be > 0")

    @property
    def x(self):
        """Get the x-coordinate of the rectangle's position."""
        return self.__x

    @x.setter
    def x(self, val):
        """
        Set the x-coordinate of the rectangle's position.

        Args:
            val (int): The new x-coordinate value.
        """
        if not type(val) is int:
            raise TypeError("x must be an integer")
        if val >= 0:
            self.__x = val
        else:
            self.__x = 0
            raise ValueError("x must be > 0")

    @property
    def y(self):
        """Get the y-coordinate of the rectangle's position."""
        return self.__y

    @y.setter
    def y(self, val):
        """
        Set the y-coordinate of the rectangle's position.

        Args:
            val (int): The new y-coordinate value.
        """
        if not type(val) is int:
            raise TypeError("y must be an integer")
        if val >= 0:
            self.__y = val
        else:
            self.__y = 0
            raise ValueError("y must be > 0")
    def area(self):
        if self.width == 0 or self.height == 0:
            return 0
        return self.height * self.width
    def display(self):
        """Print the rectangle with the # character."""

        [print("") for j in range(0,self.y)]
        for i in range(0, self.__height):
            [print(" ",end="") for i in range(0,self.x)]
            [print("#", end="") for k in range(0, self.width)]
            print("")
    def __str__(self):
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"
    def update(self, *args, **kwargs):
        j = 0
        for i, arg in enumerate(args):
            j += 1
            if i == 0:
                self.id = arg
            elif i == 1:
                self.width = arg
            elif i == 2:
                self.height = arg
            elif i == 3:
                self.x = arg
            elif i == 4:
                self.y = arg
        for k,v in kwargs.items():
            if k == "id" and j < 1:
                self.id = v
            elif k == "width"and j < 2:
                self.width = v
            elif k == "height" and j < 3:
                self.height = v
            elif k == "x"and j < 4:
                self.x = v
            elif k == "y"and j < 5:
                self.y = v
