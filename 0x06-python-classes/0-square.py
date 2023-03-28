#!/usr/bin/python3
"""Define a class Square."""

class Square:
    """Represent a square.

    Attributes:
        size (int): The size of the square.
    """
    def __init__(self, size=0):
        """Initialize a new Square object.

        Args:
            size (int): The size of the square.
        """
        self.size = size

    def area(self):
        """Return the area of the square."""
        return self.size ** 2

