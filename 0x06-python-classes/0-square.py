#!/usr/bin/python3
"""This module defines a class Square with a private attribute size and public methods."""

class Square:
    """Represents a square."""
    def __init__(self, size):
        """Initializes a new square with the given size."""
        self.__size = size

if __name__ == '__main__':
    my_square = Square()
    print((type(my_square), my_square.__dict__))


