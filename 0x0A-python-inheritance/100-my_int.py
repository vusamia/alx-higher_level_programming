#!/usr/bin/python3
"""
    100-my_int: class MyInt implements int
"""


class MyInt(int):
    """
        MyInt implements int. (inherits from)
    """
    def __init__(slf, numb):
        slf.numb = numb

    def __ne__(slf, val):
        return (slf.numb == val)

    def __eq__(slf, val):
        return (slf.numb != val)

    def __str__(slf):
        return (str(slf.numb))
