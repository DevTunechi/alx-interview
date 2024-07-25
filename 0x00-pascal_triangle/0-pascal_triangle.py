#!/usr/bin/python3
"""
0-pascal_triangle
"""


def pascal_triangle(n):
    """
    Returns a list of integers
    representing the Pascal Triangle of n
    returns empty list if n <= 0
    """
    x = []
    if n <= 0:
        return x
    x = [[1]]
    for i in range(1, n):
        temp = [1]
        for j in range(len(x[i - 1]) - 1):
            curr = x[i - 1]
            temp.append(x[i - 1][j] + x[i - 1][j + 1])
        temp.append(1)
        x.append(temp)
    return x
