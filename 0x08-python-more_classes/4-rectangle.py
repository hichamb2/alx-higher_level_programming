#!/usr/bin/python3
"""defien a class Rectangle"""


class Rectangle:
    """initialisation of Rectangle"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter of width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """setter of width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter of height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """setter of height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return (self.__height * self.__width)

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return (0)
        return ((self.__height + self.__width) * 2)

    def __str__(self):
        if self.__height == 0 or self.__width == 0:
            return ("")
        rec = []
        for i in range(self.__height):
            for j in range(self.__width):
                rec.append('#')
            rec.append("\n")
        rec.pop()
        return ("".join(rec))

    """def __repr__(self):
        return (f"Rectangle({str(self.__width)}, {str(self.__height)})")"""
