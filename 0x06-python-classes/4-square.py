#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(se, size=0):
        """Initialize a new square.
        Args:
            size (int): The size of the new square.
        """
        se.size = size

    @property
    def size(se):
        """Get/set the current size of the square."""
        return (se.__size)

    @size.setter
    def size(se, val):
        if not isinstance(val, int):
            raise TypeError("size must be an integer")
        elif val < 0:
            raise ValueError("size must be >= 0")
        se.__size = val

    def area(se):
        """Return the current area of the square."""
        return (se.__size * se.__size)
