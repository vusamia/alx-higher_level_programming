#!/usr/bin/python3
"""
    12-pascal_triangle: pascal_triangle()
"""


def pascal_triangle(n):
    """
        returns a lis of lists of integers
        Args:
            n (int): number of lists and digits
        Returns: list of lists
    """
    row_1 = [1]
    cp_l = [0]
    p_Tri = []

    if n <= 0:
        return p_Tri

    for vi in range(n):
        p_Tri.append(row_1)
        row_1 = [lm+a for lm, a in zip(row_1 + cp_l, cp_l + row_1)]
    return p_Tri
