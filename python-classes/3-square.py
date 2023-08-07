#!/usr/bin/python3
"""
class to square element
"""

class Square:
    """
    this class to representing a square
    """
    def __init__(self, size=0):
        """
        Initializes a Square class
        """
        self.__size = size

    
    def area(self):
        """
            Calculate area for this square
        """
        return (self.__size * self.__size)
    @property
    def size(self):
        """
        property to get the attribute
        """
        return self.__size
    @size.setter
    def size(self, value):
        """
        property to set the attribute
        """
        self.__size = value
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")