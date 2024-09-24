#!/usr/bin/python3
""" Island perimeter Algorithm """


def island_perimeter(grid):
    """ Calculates perimeter by checking edges of each land cell """
    pm = 0
    row = len(grid)
    col = len(grid[0])

    for r in range(row):
        for c in range(col):
            if grid[r][c] == 1:
                pm += 4
                if c < (col - 1) and grid[r][c + 1] == 1:
                    pm -= 2

                if r < (row - 1) and grid[r + 1][c] == 1:
                    pm -= 2
    return pm
