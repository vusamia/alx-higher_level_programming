#!/usr/bin/python3
"""
    101-add_attribute: add_attribute()
"""


def add_attribute(grp, nm, val):
    """
        adds a new attribute if possible.
    """
    if hasattr(grp, "__dict__") is False:
        raise TypeError("can't add new attribute")
    setattr(grp, nm, val)
