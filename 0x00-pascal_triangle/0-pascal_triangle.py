#!/usr/bin/python3
""" Solving Pascal's Triangle """


def Calc(row, col):
    """ Recursive call to calculate rows and columns """
    if col == 0 or col == row:
        return 1
    return Calc(row - 1, col - 1) + Calc(row - 1, col)


def pascal_triangle(n):
    """ Calc the pascal triangle to the nth row """
    if n <= 0:
        return []

    trg = []
    for i in range(n):
        row = [Calc(i, j) for j in range(i + 1)]
        trg.append(row)
    return trg
