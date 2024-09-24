#!/usr/bin/python3

def dfs(grid, r, c):
    if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
        return 1  # Out of bounds (water)
    if grid[r][c] == 0:
        return 1  # Water cell
    if grid[r][c] == -1:  # Already visited
        return 0

    grid[r][c] = -1

    return (dfs(grid, r - 1, c) +  # Up
            dfs(grid, r + 1, c) +  # Down
            dfs(grid, r, c - 1) +  # Left
            dfs(grid, r, c + 1))    # Right

def island_perimeter(grid):
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 1:  # Start DFS from the first land cell
                return dfs(grid, r, c)
    return 0
