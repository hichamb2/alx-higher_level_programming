#!/usr/bin/python3
"""define class Square"""


class Square:
    """initialisation class Square"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        """getter of size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """sitter of of value to size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("ize must be >= 0)")
        self.__size = value

    @property
    def position(self):
        """getter of position"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """sitter of ?? to position"""
        if (len(self.__position != 2) or not isinstance(self.__position[0], int) or not isinstance(self.__position[1], int) not isinstance(value, tuple) or value[0] < 0  or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """calcul of area"""
        return (self.__size * self.__size)

    def my_print(self):
        """difine a method that print square"""
        if self.__size == 0:
            print()
        for i in range(self.__size):
            for k in range(self.__position[0]):
                print(" ", end="")
                """if self.__position[1] > 0:
                    break"""
            for j in range(self.__size):
                print("#", end="")
            print()
