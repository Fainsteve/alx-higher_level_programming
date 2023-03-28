#!/usr/bin/python3
"""This module creates a new Square object and prints its type and dictionary."""

Square = __import__('0-square').Square

def main():
    """Create a new Square object and print its type and dictionary."""
    my_square = Square()
    print(type(my_square))
    print(my_square.__dict__)

if __name__ == '__main__':
    main()

