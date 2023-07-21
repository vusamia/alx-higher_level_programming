#!/usr/bin/python3
"""Define a MagicClass matching exactly a bytecode provided by Holberton."""

import math


class MagicClass:
    """Represent a circle."""

    def __init__(se, rad=0):
        """Initialize a MagicClass.

        Arg:
            radius (float or int): The radius of the new MagicClass.
        """
        se.__rad = 0
        if type(rad) is not int and type(rad) is not float:
            raise TypeError("radius must be a number")
        se.__rad = rad

    def area(se):
        """Return the area of the MagicClass."""
        return (se.__rad ** 2 * math.pi)

    def circumference(se):
        """Return The circumference of the MagicClass."""
        return (2 * math.pi * se.__rad)
