#!/usr/bin/python3

"""
    This module is Task 3 of the project '0x06. Python -
    Classes and Objects which is a continuation of task 2
    and adds a method to the class
"""


class Square:
    """ A Square class """
    def __init__(self, size=0):
        """ initialize square with a specific size
        Args:
            __size: size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ compute the area of a square
        Return:
            the area
        """
        return self.__size ** 2
    @property
    def size(self):
        """ getter method for the __size private instance
            attribute
        Return:
            __size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ setter method for the __size private instance
            attribute
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
