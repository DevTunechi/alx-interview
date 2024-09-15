#!/usr/bin/python3
""" Rotating a 2D matrix """


def rotate_2d_matrix(matrix):
    """ Rotate 2D matrix in 90 degrees
    """
    n = len(matrix)
    for i in range(n * n):
        r, c = divmod(i, n)
        if r < c:
            matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

    matrix[:] = [r[::-1] for r in matrix]
